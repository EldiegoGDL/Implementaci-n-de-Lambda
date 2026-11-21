# 06. Visualización de Telemetría en Grafana

Este documento proporciona la guía técnica completa para la visualización de la Arquitectura Lambda en **Grafana**: desde la conexión del Data Source hasta la solución del desfase de zona horaria y la configuración de paneles interactivos.

---

## 1. Conexión de la Base de Datos (Data Source)

Grafana consulta directamente la base de datos **PostgreSQL** de la Serving Layer:

1. Ingresa a Grafana: [http://localhost:3000](http://localhost:3000) (Usuario: `admin` / Contraseña: `admin`).
2. En el menú lateral izquierdo, haz clic en **Connections** $\rightarrow$ **Data sources** $\rightarrow$ **Add data source**.
3. Selecciona **PostgreSQL**.
4. Llena los campos de conexión:
   - **Host:** `postgres:5432` (si Grafana corre en Docker en la misma red) o `localhost:5432`.
   - **Database:** `medical_iot`
   - **User:** `admin`
   - **Password:** `admin`
   - **TLS/SSL Mode:** `disable`
5. Haz clic en el botón verde **Save & test**. Debe aparecer un banner confirmando: `Database Connection OK`.

---

## 2. Panel de Monitoreo en Tiempo Real (Speed Layer)

Este panel muestra la señal continua del electrocardiograma con los puntos de anomalía/arritmia superpuestos.

### Pasos de Configuración:
1. Menú lateral $\rightarrow$ **Dashboards** $\rightarrow$ **New** $\rightarrow$ **New Dashboard** $\rightarrow$ **Add visualization**.
2. Selecciona la fuente de datos **PostgreSQL**.
3. En la esquina superior derecha del panel, selecciona el tipo de visualización: **Time series**.
4. Cambia el editor de consultas al modo **Code** (botón de texto SQL).

---

### Las Consultas SQL con Conversión de Huso Horario

> [!IMPORTANT]
> **La Causa del Desfase de 6 Horas:**
> El script del sensor genera marcas de tiempo con `datetime.now()` (hora local de México, UTC-6). PostgreSQL almacena el valor en una columna `TIMESTAMP` sin zona horaria. Por diseño, Grafana asume que cualquier campo `TIMESTAMP` sin zona horaria viene en **UTC**, por lo que le restaba 6 horas al graficarlo en tu navegador, mostrando **"No data"** porque los datos parecían tener 6 horas de antigüedad.
> 
> La solución es indicar explícitamente a PostgreSQL: `(timestamp AT TIME ZONE 'America/Mexico_City')`. De esta forma, PostgreSQL lo convierte al instante en UTC y Grafana lo proyecta exactamente en el segundo actual de tu reloj.

#### **Query A (Línea de Ritmo Continuo):**
```sql
SELECT 
  (timestamp AT TIME ZONE 'America/Mexico_City') AS "time", 
  ecg_value 
FROM cardiac_anomalies 
WHERE $__timeFilter(timestamp AT TIME ZONE 'America/Mexico_City')
ORDER BY timestamp ASC;
```

#### **Query B (Puntos de Alerta / Arritmias):**
*(Haz clic en el botón **+ Add query** abajo del Query A)*

```sql
SELECT 
  (timestamp AT TIME ZONE 'America/Mexico_City') AS "time", 
  ecg_value AS "ANOMALÍA" 
FROM cardiac_anomalies 
WHERE $__timeFilter(timestamp AT TIME ZONE 'America/Mexico_City') AND is_anomaly = true 
ORDER BY timestamp ASC;
```

---

### Configuración del Override Visual (Puntos Rojos)

Para que las anomalías no se dibujen como una línea inconexa sino como puntos de alarma sobre el trazado:

1. En el panel de configuración de la derecha, baja hasta la sección **Overrides**.
2. Haz clic en **+ Add field override** $\rightarrow$ selecciona **Fields with name**.
3. En el desplegable, escoge **`ANOMALÍA`**.
4. Haz clic en **+ Add override property** y añade las siguientes 3 propiedades:
   - **Graph styles > Style:** Selecciona **`Points`**.
   - **Graph styles > Point size:** Escribe **`10`**.
   - **Standard options > Color scheme:** Selecciona **`Single color`** y elige el color **Rojo brillante**.
5. Haz clic en **Apply** (esquina superior derecha).

---

## 3. Panel de Tendencias Históricas (Batch Layer)

A diferencia de la Speed Layer, este panel muestra el reporte analítico consolidado día por día calculado por el procesamiento masivo del Data Lake.

### Pasos de Configuración:
1. En tu dashboard, haz clic en **Add** $\rightarrow$ **Visualization**.
2. Selecciona la base de datos **PostgreSQL**.
3. En el tipo de visualización a la derecha, selecciona **Table** (Tabla).
4. Pega la siguiente consulta en modo **Code**:

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

> [!NOTE]
> **¿Por qué esta consulta NO lleva `$__timeFilter`?**
> Como el dashboard general de tiempo real se configura en *"Last 5 minutes"*, si le pusiéramos un filtro temporal a la tabla histórica, solo intentaría mostrar los registros del día de hoy y ocultaría los días anteriores. Al no tener filtro de tiempo, siempre exhibe todo el historial de la clínica.
> 
> **¿Por qué se llama `fecha AS "Fecha"` y no `"time"`?**
> Al no usar el alias `"time"`, Grafana no lo interpreta como una serie temporal ni intenta aplicar conversiones de zona horaria, mostrando limpiamente la fecha calendario `YYYY-MM-DD`.

---

## 4. Ajustes Críticos del Dashboard (Esquina Superior Derecha)

Para que el panel se comporte como un monitor de cuidados intensivos en tiempo real:

1. **Rango de Tiempo (Time Picker):**
   - Cambia el rango a **`Last 5 minutes`** (o `Last 1 minute` para máxima resolución de la onda QRS).
2. **Auto-Refresco (Auto-Refresh):**
   - Haz clic en la flecha del ícono de recarga 🔄 y selecciona **`5s`**.
   - Con esto, cada 5 segundos Grafana solicita los nuevos latidos detectados por la Speed Layer y los dibuja en vivo.
