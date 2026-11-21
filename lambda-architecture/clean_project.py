#!/usr/bin/env python3
"""
=========================================================
SCRIPT DE LIMPIEZA TOTAL DEL PROYECTO (RESET A CERO)
=========================================================
Este script restaura el entorno de datos a su estado inicial
para permitir probar el flujo de la Arquitectura Lambda desde cero.

ACCIONES REALIZADAS:
1. Data Lake: Elimina todas las particiones diarias en data/datalake/
   (Protege explícitamente data/raw/ con el dataset clínico).
2. PostgreSQL: Trunca/Limpia las tablas 'cardiac_anomalies' y 'vitals_daily_batch'.
3. MLflow / IA: Elimina los modelos entrenados en batch/mlruns y batch/mlflow.db.
4. Kafka: Purga y recrea los tópicos 'ecg_raw' y 'vital_signs' (si Kafka está activo).
5. Cachés: Limpia carpetas __pycache__ y archivos temporales .pyc.

Nota: No modifica contenedores Docker (estos son gestionados manualmente por el usuario).
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Asegurar codificación UTF-8 en consolas Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Cargar variables de entorno si existen
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# --- COLORES PARA TERMINAL ---
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header():
    print(f"\n{CYAN}{BOLD}{'=' * 65}")
    print(" 🏥 MEDICAL IoT: RESET DEL ENTORNO DE DATOS A CERO")
    print(f"{'=' * 65}{RESET}\n")

def clean_datalake():
    """Limpia todo el contenido de data/datalake/ asegurando no tocar data/raw/"""
    print(f"{BOLD}[1/5] Limpiando Master Dataset (Data Lake)...{RESET}")
    datalake_dir = BASE_DIR / "data" / "datalake"
    raw_dir = BASE_DIR / "data" / "raw"

    # Verificación de seguridad
    if not raw_dir.exists():
        print(f"  {YELLOW}⚠️  Aviso: {raw_dir} no existe. Verifica la fuente MIT-BIH.{RESET}")
    else:
        print(f"  {GREEN}🔒 Protección activa: Dataset clínico original en '{raw_dir.relative_to(BASE_DIR)}' INTRACTO.{RESET}")

    if not datalake_dir.exists():
        datalake_dir.mkdir(parents=True, exist_ok=True)
        print(f"  {GREEN}✅ Directorio Data Lake creado vacío en: {datalake_dir.relative_to(BASE_DIR)}{RESET}")
        return

    deleted_count = 0
    for item in datalake_dir.iterdir():
        try:
            if item.is_dir():
                shutil.rmtree(item)
                deleted_count += 1
            elif item.is_file():
                item.unlink()
                deleted_count += 1
        except Exception as e:
            print(f"  {RED}❌ Error eliminando {item.name}: {e}{RESET}")

    # Asegurar que el directorio base exista vacío
    datalake_dir.mkdir(parents=True, exist_ok=True)
    print(f"  {GREEN}✅ Data Lake limpio ({deleted_count} particiones/archivos eliminados).{RESET}")

def clean_postgres():
    """Limpia las tablas en PostgreSQL si la base de datos está accesible"""
    print(f"\n{BOLD}[2/5] Limpiando Tablas en PostgreSQL (Serving Layer)...{RESET}")
    try:
        import psycopg2
    except ImportError:
        print(f"  {YELLOW}⚠️  psycopg2 no instalado en este intérprete. Omitiendo limpieza de DB.{RESET}")
        return

    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "5432"))
    dbname = os.getenv("DB_NAME", "medical_iot")
    user = os.getenv("DB_USER", "admin")
    password = os.getenv("DB_PASSWORD", "admin")

    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password,
            connect_timeout=3
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Truncar o reiniciar tablas
        tables = ["cardiac_anomalies", "vitals_daily_batch"]
        for table in tables:
            try:
                cur.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE;")
                print(f"  {GREEN}✅ Tabla '{table}' truncada a 0 registros.{RESET}")
            except Exception as e:
                # Si la tabla aún no existe, no es un error crítico
                print(f"  {CYAN}ℹ️  Tabla '{table}' no existía o no requirió truncado ({e.__class__.__name__}).{RESET}")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"  {YELLOW}ℹ️  PostgreSQL no disponible en {host}:{port} ({e.__class__.__name__}).{RESET}")
        print(f"     Si tus contenedores están detenidos, al volver a crearlos iniciarán limpios.")

def clean_mlflow(clean_models=True):
    """Elimina experimentos y modelos entrenados de MLflow"""
    print(f"\n{BOLD}[3/5] Limpiando Modelos y Experimentos (MLflow)...{RESET}")
    if not clean_models:
        print(f"  {CYAN}ℹ️  Omitido por configuración (--skip-mlflow). Modelos preservados.{RESET}")
        return

    batch_dir = BASE_DIR / "batch"
    mlruns_dir = batch_dir / "mlruns"
    mlflow_db = batch_dir / "mlflow.db"

    deleted = False
    if mlruns_dir.exists():
        try:
            shutil.rmtree(mlruns_dir)
            print(f"  {GREEN}✅ Directorio 'batch/mlruns/' eliminado.{RESET}")
            deleted = True
        except Exception as e:
            print(f"  {RED}❌ Error eliminando 'batch/mlruns/': {e}{RESET}")

    if mlflow_db.exists():
        try:
            mlflow_db.unlink()
            print(f"  {GREEN}✅ Base de datos 'batch/mlflow.db' eliminada.{RESET}")
            deleted = True
        except Exception as e:
            print(f"  {RED}❌ Error eliminando 'batch/mlflow.db': {e}{RESET}")

    if not deleted:
        print(f"  {GREEN}✅ MLflow ya se encontraba limpio (sin modelos previos).{RESET}")

def clean_kafka():
    """Purga y recrea tópicos de Kafka si el broker está activo"""
    print(f"\n{BOLD}[4/5] Verificando Tópicos de Mensajería (Kafka)...{RESET}")
    broker = os.getenv("KAFKA_BROKER", "localhost:9092")
    raw_topic = os.getenv("KAFKA_TOPIC_RAW", "ecg_raw")
    vitals_topic = os.getenv("KAFKA_TOPIC_VITALS", "vital_signs")
    topics_to_reset = [raw_topic, vitals_topic]

    try:
        from kafka.admin import KafkaAdminClient, NewTopic
        import time

        admin = KafkaAdminClient(
            bootstrap_servers=broker,
            request_timeout_ms=3000,
            client_id="project_cleaner"
        )
        existing_topics = admin.list_topics()
        topics_found = [t for t in topics_to_reset if t in existing_topics]

        if topics_found:
            admin.delete_topics(topics_found)
            print(f"  {GREEN}✅ Tópicos eliminados para purga: {topics_found}{RESET}")
            time.sleep(1) # Esperar propagación en Zookeeper/Kafka
            
            # Recrear tópicos limpios
            new_topics = [NewTopic(name=t, num_partitions=1, replication_factor=1) for t in topics_found]
            admin.create_topics(new_topics)
            print(f"  {GREEN}✅ Tópicos recreados con offset en 0: {topics_found}{RESET}")
        else:
            print(f"  {CYAN}ℹ️  Los tópicos objetivo no existían actualmente en Kafka.{RESET}")

        admin.close()
    except Exception as e:
        print(f"  {YELLOW}ℹ️  Kafka no accesible en {broker} ({e.__class__.__name__}).{RESET}")
        print(f"     Los tópicos se crearán limpios la próxima vez que inicies Kafka.")

def clean_pycache():
    """Elimina carpetas __pycache__ y archivos .pyc en todo el proyecto"""
    print(f"\n{BOLD}[5/5] Limpiando Archivos Temporales y Cachés (.pyc)...{RESET}")
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        # Ignorar entorno virtual y git
        if "venv" in root or ".git" in root:
            continue
        for d in list(dirs):
            if d == "__pycache__":
                cache_path = Path(root) / d
                try:
                    shutil.rmtree(cache_path)
                    count += 1
                except Exception:
                    pass
        for f in files:
            if f.endswith((".pyc", ".pyo")):
                file_path = Path(root) / f
                try:
                    file_path.unlink()
                    count += 1
                except Exception:
                    pass

    print(f"  {GREEN}✅ Cachés de Python eliminados ({count} elementos limpiados).{RESET}")

def main():
    parser = argparse.ArgumentParser(
        description="Limpia los datos generados del proyecto Medical IoT para ejecutarlo desde cero.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-y", "--yes", action="store_true", help="Omitir confirmación interactiva y ejecutar directamente.")
    parser.add_argument("--skip-mlflow", action="store_true", help="Conserva los modelos entrenados de MLflow (no borra batch/mlruns ni mlflow.db).")

    args = parser.parse_args()

    print_header()

    if not args.yes:
        print(f"{YELLOW}{BOLD}⚠️  ATENCIÓN:{RESET}")
        print("  Esta operación eliminará:")
        print("   - Los datos generados en el Data Lake (data/datalake/)")
        print("   - Los registros de PostgreSQL (cardiac_anomalies, vitals_daily_batch)")
        if not args.skip_mlflow:
            print("   - Los modelos y corridas de MLflow (batch/mlruns, mlflow.db)")
        print("   - Los mensajes acumulados en Kafka (si está activo)\n")
        print(f"  {GREEN}🔒 El dataset original en 'data/raw/' NO será modificado.{RESET}\n")

        try:
            confirm = input(f"{BOLD}¿Estás seguro de que deseas limpiar el proyecto desde cero? (s/N): {RESET}").strip().lower()
        except KeyboardInterrupt:
            print(f"\n{RED}Operación cancelada por el usuario.{RESET}")
            sys.exit(0)

        if confirm not in ("s", "si", "y", "yes"):
            print(f"\n{YELLOW}Operación cancelada. No se modificó ningún archivo.{RESET}\n")
            sys.exit(0)

    print()
    clean_datalake()
    clean_postgres()
    clean_mlflow(clean_models=not args.skip_mlflow)
    clean_kafka()
    clean_pycache()

    print(f"\n{GREEN}{BOLD}{'=' * 65}")
    print(" ✨ ¡PROYECTO RESTAURADO CON ÉXITO A SU ESTADO INICIAL!")
    print(f"{'=' * 65}{RESET}")
    print("Ya puedes ejecutar el flujo completo desde cero:")
    print(" 1. docker-compose up -d (si aún no has iniciado los contenedores)")
    print(" 2. python main_launcher.py (o ejecutar paso a paso según el README)\n")

if __name__ == "__main__":
    main()
