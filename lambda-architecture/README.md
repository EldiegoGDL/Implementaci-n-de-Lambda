# 🏥 Medical IoT: Arquitectura Lambda Pura
### *Detección de Arritmias en Tiempo Real con Machine Learning*

![Python](https://img.shields.io/badge/Python-3.12-green.svg)
![Kafka](https://img.shields.io/badge/Streaming-Kafka-orange.svg)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)

Este proyecto implementa una **Arquitectura Lambda** completa para la ingestión, procesamiento y análisis de señales de electrocardiograma (ECG) en tiempo real. Utilizando datos clínicos del dataset **MIT-BIH**, el sistema bifurca el flujo de datos para ofrecer tanto respuestas inmediatas (Speed Layer) como análisis precisos de largo plazo (Batch Layer).

---

## 🏗️ Arquitectura del Sistema

El flujo de datos sigue el patrón estándar de la Arquitectura Lambda para garantizar escalabilidad y tolerancia a fallos:

- **📡 Fuente de Datos (Sensor):** Script en `data_sources/sensor_simulador.py` que simula un monitor Holter procesando archivos médicos `.dat` y enviando telemetría continua vía Kafka.
- **📥 Capa de Ingesta:** Apache Kafka gestiona el flujo de alta velocidad de los datos biométricos.
- **⚡ Speed Layer (Tiempo Real):** Inferencia en milisegundos mediante un modelo *Isolation Forest* (gestionado vía MLflow en el puerto 5001) para detección de anomalías usando una **Ventana Deslizante**.
- **📊 Batch Layer (Data Lake & Histórico):** Almacenamiento inmutable (retención `earliest`) para el cálculo diario de la "verdad absoluta" mediante procesamiento pesado.
- **🌐 Serving Layer:** PostgreSQL y FastAPI (`serving/query_api.py`) unifican ambas capas para exponer una vista clínica consolidada (Merge).

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
| :--- | :--- |
| **Streaming** | Apache Kafka |
| **Model Serving** | MLflow |
| **Procesamiento** | Python 3.12 (Pandas, Scikit-Learn, WFDB) |
| **Almacenamiento** | PostgreSQL (Data Lake en JSONL) |
| **Visualización** | Grafana |
| **API** | FastAPI |
| **Contenerización** | Docker & Docker Compose |

---

## 📁 Estructura del Proyecto

```text
lambda-architecture/
├── 📂 batch/            # Entrenamiento de IA (train_model.py), orquestador y proceso diario
├── 📂 data/             # Datos crudos (MIT-BIH), Data Lake inmutable y persistencia BD
├── 📂 data_sources/     # Script simulador de sensor escalable (sensor_simulador.py)
├── 📂 serving/          # API REST para consulta de vistas unificadas (query_api.py)
├── 📂 streaming/        # Speed Layer (anomaly_detector.py) y persistencia (raw_to_datalake.py)
├── 📄 main_launcher.py  # GUI de Control (Command Center)
├── 📄 docker-compose.yml # Orquestación de infraestructura (Kafka, DB, MLflow en p5001)
├── 📄 requirements.txt  # Dependencias del proyecto (usa kafka-python-ng)
└── 📄 .env.example      # Plantilla de variables de entorno
```

---

## ⚙️ Instalación y Configuración

> **⚠️ Requisito Estricto de Python:** Se debe utilizar **Python 3.12**. Las librerías de procesamiento de señales y Machine Learning (`wfdb`, `numpy`, `scipy`, `scikit-learn`) dependen de extensiones binarias C compiladas para Python 3.12. Versiones superiores (como 3.13 o 3.14) causarán incompatibilidades binarias al importar NumPy o WFDB. Además, asegúrate de tener Docker Desktop instalado y en ejecución.

### 1. Variables de Entorno

Copia la plantilla de variables de entorno y ajusta las credenciales si es necesario:

```bash
cp .env.example .env
```

### 2. Preparar el Entorno e Instalar Dependencias (¡Paso Crítico con Python 3.12!)

Para asegurar que todo funcione sin conflictos de versiones, **crea el entorno virtual explícitamente con Python 3.12**:

```powershell
# 1. Crear el entorno virtual con Python 3.12
py -3.12 -m venv venv

# 2. Activar el entorno virtual
.\venv\Scripts\Activate.ps1
# (O en CMD clásico: venv\Scripts\activate.bat)

# 3. Instalar las dependencias exactas
pip install -r requirements.txt
```

### 3. Configurar Base de Datos MLflow y Datos Médicos

- Crea un archivo vacío llamado `mlflow.db` en la carpeta `batch/`.
- Descarga `100.dat` y `100.hea` de [MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/).
- Colócalos en `data/raw/`.

---

## 🚀 Guía de Ejecución

Abre terminales separadas para ejecutar los componentes y observar el flujo de la arquitectura en acción:
Procura siempre estar en el entorno previamente creado, de lo contrario generara conflicto

### Paso 1: Levantar Infraestructura

```bash
docker-compose up -d
```

Espera ~30s a que Kafka inicie. MLflow estará disponible en `http://localhost:5001`.
Despues de los 30s puede suceder que kafka no haya iniciado, revisa manualmente en Docker Desktop para confirmarlo o bien, iniciarlo

### Paso 2: Entrenar el Modelo *(Requisito para Speed Layer)*

```bash
python batch/train_model.py
```

### Paso 3: Levantar la Serving Layer

```bash
python serving/query_api.py
```

### Paso 4: Iniciar el Flujo de Datos

```bash
# Fuente de Datos
python data_sources/sensor_simulador.py

# Data Lake
python streaming/raw_to_datalake.py

# Speed Layer
python streaming/anomaly_detector.py

# Orquestador Batch
python batch/scheduler.py
```

> **Nota:** Si usas la GUI `main_launcher.py`, puedes omitir el Paso 3 y 4 y controlar los procesos directamente desde la interfaz. Aun asi, se aconseja encarecidamente utilizar los comandos propuestos para tener un mejor entendimiento del funcionamiento de la arquitectura y facilitar la depuración de errores.

---

## 📊 Visualización y Consultas

### API (Serving Layer)

- **Swagger UI:** `http://localhost:8000/docs`
- **Endpoint Unificado (Merge Lambda):** `GET /unified/{patient_id}` *(Prueba con `PACIENTE-100`)*

### Grafana

**URL:** `http://localhost:3000` (usuario: `admin` / contraseña: `admin`)

Para visualizar correctamente el flujo de datos y las alertas, sigue estos pasos de configuración en el dashboard:

#### 1. Conexión de la Base de Datos (Data Source)
- Click en Menu
- Connections -> Add new connection
- click en PostgreSQL
- **Host:** `postgres:5432` (si usas Docker) o `localhost:5432`
- **Database:** `medical_iot` | **User:** `admin` | **Password:** `admin`
- **TLS/SSL Mode:** disable
- **Paso Crítico:** Haz clic en *Save & Test*. Si aparece en verde, la comunicación con la base de datos es exitosa.

#### 2. Panel de Monitoreo en Tiempo Real (Speed Layer)
- Click en Menu
- Click en Dashboards
- Click en New -> New Dashboard
- Click en Add visualization
- Selecciona la base de datos PostgreSQL

Para ver la señal de ECG y los puntos de anomalía superpuestos en la misma gráfica:
- **Tipo de Visualización:** Time series

**Query A (Línea de Ritmo Continuo):**
```sql
SELECT 
  (timestamp AT TIME ZONE 'America/Mexico_City') AS "time", 
  ecg_value 
FROM cardiac_anomalies 
WHERE $__timeFilter(timestamp AT TIME ZONE 'America/Mexico_City')
ORDER BY timestamp ASC;
```

**Query B (Puntos de Alerta):**
```sql
SELECT 
  (timestamp AT TIME ZONE 'America/Mexico_City') AS "time", 
  ecg_value AS "ANOMALÍA" 
FROM cardiac_anomalies 
WHERE $__timeFilter(timestamp AT TIME ZONE 'America/Mexico_City') AND is_anomaly = true 
ORDER BY timestamp ASC;
```


- **Ajuste de Estilo (Panel de la derecha):** Para la serie "ANOMALÍA", ve a *Overrides* y añade una regla "fields with name", escoges ANOMALIA, click en Add override property escoges "Graph styles > Style" y seleccionas *Points*, despues click en Add override property escoges "Graph styles > Point size", lo pones en 10,  y el color sea *Rojo Intenso*, click en Add override property y escoges "Standard options > Color" y seleccionas el color rojo. Esto dibujará un punto sobre la línea cada vez que el modelo detecte una arritmia. Click en Apply



#### 3. Panel de Tendencias Históricas (Batch Layer)
- Damos click en el boton Add > Visualization
- **Tipo de Visualización:** Table (Tabla) o Stat

**Query:**
```sql
SELECT 
  fecha AS "Fecha",
  patient_id AS "Paciente",
  total_muestras AS "Muestras Procesadas",
  ROUND(promedio_ecg::numeric, 4) AS "Media ECG", 
  max_ecg AS "Pico Máximo", 
  min_ecg AS "Pico Mínimo"
FROM vitals_daily_batch 
ORDER BY fecha DESC;
```

#### 4. Notas para evitar fallos de visualización
- **Rango de Tiempo:** En la esquina superior derecha de Grafana, asegúrate de cambiar el rango a "Last 5 minutes" o "Last 15 minutes". Por defecto suele estar en 6 horas y los datos nuevos se ven como una línea muy pequeña al final.
- **Auto-Refresh:** Activa la actualización automática (ícono de reloj arriba a la derecha) cada 5 segundos para ver el "latido" del sistema en vivo.

---

## 🔧 Solución de Problemas Frecuentes

| Error | Solución |
| :--- | :--- |
| `Importing the numpy C-extensions failed` / `No module named 'numpy._core._multiarray_umath'` | El entorno virtual se creó con una versión distinta (ej. Python 3.14). Recrea el entorno estrictamente con Python 3.12: `py -3.12 -m venv venv --clear`. |
| `No module named 'kafka.vendor.six.moves'` | Desinstala `kafka-python` e instala `kafka-python-ng` (compatibilidad Python 3.12+). |
| `RESOURCE_DOES_NOT_EXIST: Run with id=latest` | Ejecuta `python batch/train_model.py` primero para registrar el modelo en la versión 1. |
| `MLflow connection error` | Asegúrate de que el puerto `5001` esté mapeado en `docker-compose.yml` y en tu archivo `.env`. |
| `NoBrokersAvailable` | Kafka tarda ~30s en iniciar dentro de Docker. Espera un momento y reintenta el script del sensor. |

---

## 📝 Justificación Arquitectónica

Este proyecto se adhiere a los pilares fundamentales de la Arquitectura Lambda:

- **Inmutabilidad:** Los datos en el Data Lake nunca se modifican, solo se añaden de forma segura (tolerancia a fallos con offset `earliest`).
- **Precisión:** La Batch Layer corrige cualquier posible deriva mediante un procesamiento pesado consolidado.
- **Inmediatez:** La Speed Layer (Ventana Deslizante) proporciona alertas críticas en milisegundos, latido a latido.
