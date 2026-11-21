# 📚 Documentación Técnica: Medical IoT - Arquitectura Lambda

Bienvenido a la suite de documentación técnica del proyecto **Medical IoT: Detección de Arritmias Cardíacas en Tiempo Real y Análisis Histórico mediante Arquitectura Lambda**.

Este repositorio implementa una solución completa de ingeniería de datos y aprendizaje automático (*Machine Learning*) para procesar señales biomédicas de electrocardiograma (ECG), balanceando la necesidad de **inmediatez de alertas críticas en milisegundos** con la **precisión estadística histórica inmutable**.

---

## 🗺️ Mapa de Navegación de la Documentación

La documentación está organizada en 7 módulos especializados diseñados para explicar desde la teoría arquitectónica de Big Data hasta la operación y el código fuente:

```
docs/
├── 01_fundamentos_arquitectura_lambda.md   # Marco teórico, Teorema de Nathan Marz, Diagrama global y Lambda vs Kappa
├── 02_fuente_datos_y_kafka.md              # Dataset clínico MIT-BIH, simulador IoT y clúster Apache Kafka
├── 03_speed_layer_ia.md                    # Detección de arritmias en vivo, Isolation Forest y registro MLOps en MLflow
├── 04_batch_layer_y_datalake.md            # Master Dataset inmutable en JSONL, agregaciones con Pandas y Scheduler
├── 05_serving_layer_fastapi.md             # API RESTful, patrón Merge Lambda (/unified/{patient_id}) y esquema PostgreSQL
├── 06_visualizacion_grafana.md             # Paneles de telemetría en tiempo real, resolución de huso horario y reportes
└── 07_guia_operacion_y_solucion_fallos.md  # Launcher interactivo, ejecución por CLI, script de reset y troubleshooting
```

---

## 📖 Resumen Rápido de los Módulos

### [1. Fundamentos de la Arquitectura Lambda](01_fundamentos_arquitectura_lambda.md)
Descubre los principios teóricos propuestos por Nathan Marz, la ecuación fundamental de consulta $Query = F(\text{All Data})$, el diagrama de flujo general del sistema y la justificación técnica de por qué se eligió la arquitectura Lambda sobre la arquitectura Kappa en un contexto médico hospitalario.

### [2. Fuente de Datos y Streaming Ingestion (Kafka)](02_fuente_datos_y_kafka.md)
Explicación detallada de la base de datos clínica de arritmias del MIT-BIH (`data/raw/100`), el módulo simulador de sensores de grado médico (`data_sources/sensor_simulador.py`) y la configuración de tópicos de Apache Kafka con Zookeeper.

### [3. Speed Layer & Detección de Anomalías con IA](03_speed_layer_ia.md)
Cómo funciona la capa de baja latencia (`streaming/anomaly_detector.py`): mecanismo de ventana deslizante en memoria (*sliding window* de 100 muestras), algoritmo de Isolation Forest para detección no supervisada de latidos irregulares y gestión del ciclo de vida del modelo en MLflow.

### [4. Batch Layer & Master Dataset (Data Lake)](04_batch_layer_y_datalake.md)
La garantía de verdad absoluta: ingesta inmutable tolerante a fallos (`streaming/raw_to_datalake.py` con offset `earliest`), particionado cronológico diario en archivos JSON Lines y procesamiento pesado de agregaciones con Pandas (`batch/batch_daily_processor.py` y `batch/scheduler.py`).

### [5. Serving Layer & API RESTful (FastAPI)](05_serving_layer_fastapi.md)
La capa de servicio (`serving/query_api.py`) que expone los datos a aplicaciones médicas externas. Destaca el endpoint unificado `/unified/{patient_id}`, donde se fusionan las métricas históricas de 7 días con las alertas en tiempo real del día de hoy (*Merge Lambda*).

### [6. Visualización de Telemetría en Grafana](06_visualizacion_grafana.md)
Guía paso a paso para configurar los paneles de monitoreo en Grafana: la gráfica de ritmo cardíaco continuo superpuesta con puntos rojos de arritmia, la tabla de reportes clínicos diarios y la resolución técnica al desfase de zona horaria de 6 horas UTC.

### [7. Guía de Operación y Solución de Fallos](07_guia_operacion_y_solucion_fallos.md)
Manual operativo completo: ejecución a través del Centro de Comando Gráfico (`main_launcher.py`), ejecución desacoplada por terminales independientes, uso del script de limpieza total (`clean_project.py`) y bitácora de solución a errores técnicos reales (Python 3.12 selector fix, Docker broker readiness, etc.).

---

## 🛠️ Stack Tecnológico Integrado

| Componente | Tecnología | Rol en la Arquitectura |
| :--- | :--- | :--- |
| **Fuente de Datos** | WFDB / Python | Simulación de telemetría de biosensores hospitalarios |
| **Message Broker** | Apache Kafka 7.4.0 & Zookeeper | Ingesta de eventos a escala con buffers distribuidos |
| **Master Dataset** | Data Lake local (JSON Lines) | Almacenamiento inmutable y append-only (Verdad Histórica) |
| **Machine Learning** | Scikit-Learn (Isolation Forest) | Detección no supervisada de anomalías en tiempo real |
| **MLOps & Tracking** | MLflow 2.10+ | Registro centralizado y versionado de modelos de IA |
| **Batch Processing** | Python & Pandas | Procesamiento analítico pesado y cálculos estadísticos diarios |
| **Serving Database** | PostgreSQL 15 | Almacenamiento relacional de vistas batch y speed |
| **API RESTful** | FastAPI & Uvicorn | Exposición de endpoints y fusión de vistas (*Merge Lambda*) |
| **Visualización** | Grafana 10.0.0 | Tablero clínico interactivo de alta frecuencia |
| **Orquestación GUI** | Tkinter / Threading / Queue | Centro de control educativo con métricas de salud en vivo |
