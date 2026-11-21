# Manual de laboratorio: desarrolla con un agente de IA

## Del repositorio Lambda a una mejora probada y documentada

**Arquitectura de Software · Ingeniería de Software · UAZ**  
Versión 3.0 · 18 de noviembre de 2026  
Repositorio de trabajo: <https://github.com/jrruiz68/lambda-architecture>

En este laboratorio vas a conectar un agente de programación a tu copia del proyecto. Le pedirás que explore archivos, ejecute comprobaciones, construya herramientas, te ayude a corregir problemas y prepare documentación a partir de lo que realmente hicieron.

El agente puede escribir el código, los diagramas y los documentos. Tu trabajo es darle objetivos y contexto, revisar sus decisiones, comprobar el resultado y dirigir la siguiente iteración. No necesitas comenzar llenando un reporte ni redactando todos los documentos a mano.

**Ruta principal:** Codex en Visual Studio Code, trabajando sobre la computadora donde ejecutas Lambda. Se incluye una alternativa por terminal. Si ya tienes otro agente con lectura de archivos, edición y terminal, puedes usar los mismos ejercicios y adaptar su configuración.

### Qué vas a construir

La práctica se concentra en dos resultados: **una mejora acotada, diseñada y probada con apoyo de un agente**, y **un reporte individual en Markdown** con las vistas estática, física y dinámica actualizadas para la versión entregada. La mejora puede atender una necesidad funcional, de portabilidad entre sistemas operativos, de configuración, pruebas, observabilidad o documentación ejecutable. Debe ser pertinente al proyecto y conservar sus responsabilidades y límites arquitectónicos.

| Momento | Trabajo principal | Evidencia que queda |
|---|---|---|
| Hasta el sábado 21 de noviembre | Conectar el agente, revisar el estado real del repositorio, dibujar las tres vistas actuales y acordar una propuesta pequeña. | `AVANCE_SABADO.md`: entorno y commit, vistas iniciales, problema observado, propuesta, impacto previsto y criterios de aceptación. |
| Semana 2 · 23–28 de noviembre | Implementar en pasos pequeños una mejora acordada; probar el comportamiento anterior y el nuevo; documentar lo realmente ejecutado. | Código revisado, pruebas o comprobaciones con resultados observados, y ajustes de portabilidad si aplican. |
| Semana 3 · 30 de noviembre–5 de diciembre | Cerrar el cambio, pedir una revisión al agente, actualizar las tres vistas según la implementación final y completar el análisis individual. | `REPORTE_INDIVIDUAL.md`, instrucciones reproducibles y versión final identificada por commit. |

**Avance específico para este sábado:** no se espera terminar la implementación. Cada estudiante debe llegar con el agente conectado a su copia, el estado inicial protegido, tres diagramas preliminares de la arquitectura existente y una propuesta viable para la mejora. El equipo puede acordar una mejora común, pero cada integrante conserva evidencia de su revisión y redacta su propio reporte. Si alguien trabaja individualmente, realiza ambos productos por su cuenta.

La carga sugerida es de aproximadamente **5–7 horas fuera de las sesiones durante las tres semanas**, distribuida según el tiempo disponible. Si el entorno presenta problemas, se reportan y se acota la mejora; no se compensa una instalación difícil con cambios grandes ni con horas de trabajo no previstas. Los ejercicios de diagnóstico automático y de laboratorio de datos que aparecen más adelante son recursos opcionales: no son entregables obligatorios de esta versión.

## Calendario de trabajo

### De hoy al sábado 21 de noviembre · comprender y proponer

1. **Conecta el agente y comprueba sus capacidades** con un archivo inocuo del repositorio. Registra herramienta y límites observados.
2. **Guarda el estado de partida:** rama, commit y cambios locales. Conserva arreglos previos; no sobrescribas ni limpies el trabajo existente.
3. **Pide al agente un mapa de arquitectura actual** con las vistas estática, física y dinámica. Comprueba en el código o configuración al menos una relación importante de cada vista.
4. **Elige un problema pequeño con evidencia.** Puede ser un ajuste de compatibilidad que hayan encontrado, una mejora funcional acotada u otra necesidad del proyecto.
5. **Define una propuesta y criterios observables.** Identifica elementos y contratos que podrían tocarse, lo que queda fuera del alcance, cómo se probará y qué significaría preservar la arquitectura.

**Entrega del sábado:** usa `plantillas/AVANCE_SABADO.md` como base para crear `docs/laboratorio_llm/AVANCE_SABADO.md`, con identificación del repositorio, entorno, resumen de cambios previos a conservar, los tres diagramas *antes del cambio*, problema y evidencia, mejora propuesta, alcance y exclusiones, impacto esperado en las tres vistas, criterios de aceptación, pruebas previstas y preguntas pendientes. Si una vista no puede confirmarse todavía, se etiqueta como pendiente y se explica cómo se verificará.

**Mensaje para preparar el avance con el agente:**

```text
Lee primero AGENTS.md y docs/laboratorio_llm/CONTEXTO.md si existen. Inspecciona
la rama, el commit, los cambios locales, la configuración y los archivos reales.
No modifiques código ni sobrescribas cambios previos. Usa la plantilla
plantillas/AVANCE_SABADO.md para generar docs/laboratorio_llm/AVANCE_SABADO.md.
Completa las vistas estática, física y dinámica solo con elementos observados;
vincula cajas y relaciones con código/configuración. Etiqueta hechos, inferencias
y pendientes. Señala cualquier error por sistema operativo con SO, versión,
comando y salida observada. Propón una mejora acotada basada en evidencia,
con exclusiones, efecto previsto en cada vista, contratos que deben preservarse
y criterios de aceptación comprobables. No elijas ni implementes la propuesta
por mí: termina con las decisiones y preguntas que el equipo debe resolver.
```

Revisa los tres diagramas: el agente puede producir Mermaid, pero tú confirmas
que los nombres existan y que las flechas correspondan a un flujo real. Una
vista preliminar incompleta es mejor que una vista inventada; deja la duda
registrada y acuerda cómo verificarla antes de implementar.

### Semana 2 · 23–28 de noviembre · implementar y comprobar

- Trabaja sobre una rama o punto de control identificable. Pide al agente primero un plan de archivos y pasos; revisa ese plan antes de autorizar la edición.
- Implementa solamente la mejora acordada. Revisa cada diff y separa cambios no relacionados.
- Ejecuta las pruebas pertinentes en el entorno disponible. Registra comando, sistema operativo, resultado esperado, resultado observado y limitaciones. No afirmes compatibilidad en sistemas que no hayas probado.
- Revisa si el cambio alteró responsabilidades, interfaces, despliegue, configuración o recorrido de ejecución. Si el diseño cambia, actualiza los diagramas en borrador; la versión final se cerrará en la semana 3.

### Semana 3 · 30 de noviembre–5 de diciembre · revisar y explicar

- Solicita al agente una revisión crítica del diff y corrige o justifica los hallazgos.
- Actualiza desde la versión final las vistas estática, física y dinámica. Deben describir lo implementado, no solamente el diseño propuesto.
- Cada estudiante completa su propio `REPORTE_INDIVIDUAL.md`, con referencias a archivos, pruebas y commit. El agente puede ayudar a redactarlo, pero el estudiante comprueba diagramas, resultados y decisiones.
- Comprueba que otra persona pueda seguir las instrucciones básicas de ejecución y localice el resultado esperado. Guarda el commit final y prepara una explicación breve de la mejora y de sus efectos arquitectónicos.

**Una mejora pequeña y comprobada es suficiente.** No es requisito añadir servicios, migrar tecnologías, reescribir la arquitectura, probar todos los sistemas operativos ni ejecutar una plataforma distribuida completa. Si una prueba depende de infraestructura no disponible, documenta el bloqueo y prepara una comprobación sustituta que indique con claridad qué parte sí valida.

---

## Antes de empezar: distingue dónde se hacen las cosas

En el manual hay dos tipos de bloques:

- **Terminal:** comandos que ejecutas en la terminal del proyecto. También puedes pedir al agente que los ejecute cuando ya tenga acceso.
- **Mensaje al agente:** texto que copias en su conversación. No se pega en PowerShell, Bash ni otra terminal como si fuera un comando.

Un agente usa un modelo de lenguaje y herramientas. Puede leer archivos, editar y ejecutar comandos cuando su entorno y permisos lo permiten. La forma de comprobar esas capacidades será una acción observable, no solamente preguntarle si puede hacerlo.

### Qué necesitas

1. Tu copia del repositorio, incluyendo los ajustes que ya hiciste.
2. Un editor y acceso a un agente de programación. La ruta explicada usa Visual Studio Code y la extensión oficial de Codex.
3. Git para guardar cambios. Si aún no lo tienes, instala la distribución correspondiente a tu sistema antes de usar sus comandos.
4. Las herramientas necesarias para ejecutar Lambda cuando llegues a esa etapa: Python, dependencias y servicios del proyecto. El agente te ayudará a revisar qué está disponible.

No necesitas entrenar un LLM ni incorporar una API de LLM al sistema Lambda. En esta práctica, el agente es tu herramienta de desarrollo. La cuenta y el método de acceso dependen de la herramienta elegida: usa el acceso que ya tengas disponible y verifica sus límites antes de contratar un servicio.

### Conserva lo que ya funciona

Si ya tienes el proyecto, trabaja sobre esa copia. No lo clones de nuevo para perder los arreglos que hiciste. Abre una terminal en la carpeta y ejecuta por separado:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
```

Estos comandos muestran cambios locales, rama y commit. Una rama nueva **no guarda por sí sola** los cambios sin commit. Antes de una intervención grande, revisa los archivos modificados y guarda un punto de control con los archivos pertinentes; evita incluir `.env`, entornos virtuales y datos generados.

Si todavía no tienes una copia, puedes crear un fork desde GitHub si necesitas publicar en tu propio repositorio. Para una copia local de lectura y trabajo puedes clonar el original:

```bash
git clone https://github.com/jrruiz68/lambda-architecture.git
cd lambda-architecture
git switch -c laboratorio-llm
```

Clonar el original no te da permiso para subir cambios a él. Tu entrega puede residir en tu fork. Si la rama ya existe, conserva la que estás usando o selecciona otro nombre; no borres trabajo para repetir estos pasos.

---

## 1. Conecta el agente y verifica que trabaja en tu repositorio

### Ruta A. Codex dentro de Visual Studio Code

1. Abre Visual Studio Code y selecciona **Archivo / File → Abrir carpeta / Open Folder**. Elige la raíz de `lambda-architecture`, donde está `README.md`.
2. Instala la extensión oficial desde el enlace de la [documentación de Codex para IDE](https://learn.chatgpt.com/docs/codex/ide). Comprueba que corresponde a OpenAI.
3. Abre el panel de Codex. Si no aparece, abre la paleta de comandos y busca **Codex: Open Codex Sidebar**.
4. Selecciona **Sign in with ChatGPT** y completa el inicio de sesión en el navegador. También existen métodos con API key; el acceso por API tiene su propia facturación. Para esta práctica no pegues claves en el prompt ni en el código. Consulta [autenticación](https://learn.chatgpt.com/docs/auth).
5. Trabaja en el proyecto local. Empieza con inspección; cuando solicites crear archivos o ejecutar pruebas, revisa los permisos disponibles para ese proyecto. El [control de permisos](https://learn.chatgpt.com/docs/agent-approvals-security) define qué acciones puede ejecutar el agente.

Ahora envía este **mensaje al agente**:

```text
Estamos en una práctica de Arquitectura de Software. Primero comprueba el
proyecto abierto. No cambies archivos todavía.

1. Indica tu directorio de trabajo, la raíz Git y el commit actual.
2. Lee README.md, docker-compose.yml y requirements.txt.
3. Abre serving/query_api.py y localiza una ruta HTTP real y la función
   que la implementa. Muéstrame el nombre de la función y un fragmento breve.
4. Ejecuta git status --short y explica qué cambios ya existen.
5. Indica si tus comandos corren en mi equipo, en WSL, en un contenedor
   o en un entorno remoto. Si no puedes comprobarlo, dilo.

No instales dependencias ni imprimas el contenido de .env.
```

**Comprueba tú:** abre el archivo y busca la ruta que mencionó. En la versión de referencia hay una ruta `/unified/{patient_id}`; tu copia puede haber cambiado. Debe mostrar una lectura o ejecución real en el historial de acciones. Si solamente propone comandos, todavía no ha demostrado que tenga terminal.

**Prueba de escritura — mensaje al agente:**

```text
Crea docs/laboratorio_llm/CONEXION.md. Registra únicamente las capacidades
que acabas de comprobar: lectura, terminal, escritura, ubicación de ejecución
y commit. Omite rutas personales innecesarias. Si alguna capacidad no está
disponible, indícala. No modifiques archivos de aplicación.
```

Abre `CONEXION.md` en el explorador del editor. Ya tienes una primera acción verificable del agente sobre tu proyecto.

### Ruta B. Codex desde la terminal

Si prefieres terminal, instala Codex con uno de los métodos de la [guía oficial CLI](https://learn.chatgpt.com/docs/codex/cli). Si ya tienes Node.js y npm disponibles, un método documentado es:

```bash
npm install -g @openai/codex
```

Después, desde la carpeta del repositorio:

```bash
codex
```

Completa el inicio de sesión ofrecido por el cliente y envía los mismos mensajes de comprobación. La instalación del agente y el entorno virtual de Python del proyecto son cosas distintas. Si eliges otra forma de instalación, sigue la variante oficial para tu sistema operativo.

### Si usas otro agente o un entorno en la nube

Usa los mismos mensajes para comprobar lectura, edición, ejecución y ubicación. Un chat con archivos adjuntos puede analizar esos archivos; comprueba por separado si puede modificar el repositorio y ejecutar pruebas.

En [Codex Cloud](https://learn.chatgpt.com/docs/cloud), el código se trabaja en un entorno remoto que debe tener sus propios datos y herramientas. Un `localhost` de ese entorno no es automáticamente tu computadora. Para los problemas de Windows, macOS o Linux que encontraste en clase, ejecuta la comprobación en el entorno realmente afectado. Una prueba remota no certifica que tu Docker local o tu interfaz gráfica funcionen.

### Si algo falla en la conexión

| Lo que observas | Siguiente acción |
|---|---|
| No aparece el panel. | Comprueba la extensión instalada, abre la paleta y busca el comando indicado. |
| El agente no encuentra los archivos. | Revisa la carpeta abierta y pídele que liste sus rutas; puede estar en otro proyecto. |
| Describe comandos pero no los ejecuta. | Revisa capacidades y permisos; si no hay terminal, ejecútalos tú y proporciona la salida. |
| Ve una versión distinta. | Compara rama, commit y cambios sin commit entre ambos entornos. |
| No puede conectarse a Docker o a la red. | Identifica si es un permiso, un servicio apagado o un entorno distinto antes de cambiar código. |
| Pide acceso o pago que no tienes. | Usa otra herramienta disponible o consulta con la docente; no compartas cuentas o claves. |

**Terminas esta etapa cuando:** el agente encuentra código real y puedes abrir el archivo que creó. Si la terminal es manual, esa limitación queda declarada.

---

## 2. Enséñale cómo trabajar y deja memoria útil

Vas a separar dos cosas: instrucciones que se mantienen y hechos que cambian durante el trabajo.

| Archivo | Contenido | Quién lo prepara |
|---|---|---|
| `AGENTS.md`, en la raíz | Acuerdos de trabajo: alcance, revisión, pruebas y documentación. | El agente genera un borrador y el equipo lo revisa. |
| `docs/laboratorio_llm/CONTEXTO.md` | Entorno confirmado, ajustes previos, estado y siguiente paso. | El agente lo actualiza con datos observados y confirmaciones del equipo. |

Codex reconoce `AGENTS.md` como instrucciones del proyecto y puede combinarlo con instrucciones de otras carpetas. `CONTEXTO.md` es una convención de esta práctica: hay que pedir que lo lea. Mantén ambos breves. La [guía de AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) describe su alcance y carga al iniciar una sesión.

**Mensaje al agente:**

```text
Prepara el contexto de esta práctica. Revisa primero si ya existe AGENTS.md;
si existe, conserva sus reglas y propón una integración compatible.

En AGENTS.md deja estos acuerdos de forma breve:
- Leer docs/laboratorio_llm/CONTEXTO.md al comenzar.
- Conservar mis cambios existentes y trabajar en la tarea solicitada.
- Examinar el código antes de afirmar qué hace el sistema.
- Usar el intérprete y la terminal confirmados para este proyecto.
- Para un cambio, explicar su propósito, revisar el diff y ejecutar una
  comprobación pertinente. Si no se ejecutó, declararlo.
- Documentar los comandos que realmente funcionaron y los límites encontrados.
- No publicar secretos ni hacer push, borrados de datos o cambios globales
  del sistema sin que se solicite esa acción.

Genera CONTEXTO.md a partir del repositorio y de comprobaciones de lectura.
Incluye SO, CPU, shell, Python e intérprete, Docker/Compose si están disponibles,
rama, commit, cambios locales y estado actual. No imprimas credenciales.
Pregunta solo por información indispensable que no puedas obtener.
Deja pendientes visibles; no inventes mis decisiones ni mi participación.
```

**Si quieres empezar desde los archivos del paquete:** puedes usar `plantillas/AGENTS.inicial.md` como base para el `AGENTS.md` de la raíz y `plantillas/CONTEXTO.inicial.md` como base del contexto. No sustituyas un archivo existente sin integrar sus reglas. No tienes que llenar esos archivos a mano: el mensaje anterior guía al agente.

Revisa que no haya anotado versiones por suposición. Si Windows ejecuta una terminal WSL, deben aparecer ambos datos. Si cambiaste las instrucciones durante una sesión, pide al agente que relea los archivos; una nueva sesión debe comenzar confirmando qué instrucciones cargó.

**Terminas esta etapa cuando:** puedes abrir una conversación nueva, pedir que lea esos dos archivos y recuperar el estado del proyecto sin pegar toda la conversación anterior.

---

## 3. Convierte el repositorio en un mapa que puedas explicar

La primera tarea de exploración será producir documentación desde el código. El objetivo es descubrir responsabilidades y conexiones que podrás verificar.

**Mensaje al agente:**

```text
Explora la implementación actual de Lambda. No cambies el código.
Genera docs/laboratorio_llm/ARQUITECTURA.md con:

1. Un resumen del propósito del sistema y un mapa de archivos clave.
2. Un diagrama de contenedores en Mermaid: procesos ejecutables, almacenes,
   tecnologías y conexiones. Un contenedor C4 no equivale siempre a Docker.
3. Una tabla: elemento, responsabilidad, archivo/función, entrada y salida.
4. El recorrido de una muestra desde el simulador hasta una consulta.
5. Dónde se ejecuta cada proceso: anfitrión, Docker u otro entorno.
6. Dos preguntas sobre comportamientos que el código o la documentación
   no permitan asegurar todavía, y cómo podríamos comprobarlos.

Separa arquitectura existente y propuestas. Cada elemento debe relacionarse
con código o configuración. No dibujes servicios solamente porque son
habituales en una arquitectura Lambda. Añade descripción textual del diagrama.
```

**Haz esta comprobación:** selecciona dos flechas del diagrama y pide al agente que abra el código que las respalda. Por ejemplo, quién escribe los datos crudos y quién lee los resultados batch. Si no hay una relación implementada, corrige el diagrama.

**Mensaje para profundizar:**

```text
Explícame qué ocurriría con la consulta si el proceso batch deja de ejecutarse.
Localiza los archivos que sustentan tu explicación y distingue lo que sabes
por inspección de lo que necesitaríamos medir. Después hazme una pregunta
sobre ese recorrido y espera mi respuesta antes de explicarla.
```

**Resultado:** un documento visual generado por el agente, revisado por el equipo. No necesitas exigir cuatro niveles C4 ni un diagrama de clases completo para entender esta implementación.

---

## 4. Recurso opcional: construye un diagnóstico automático del proyecto

Este ejercicio es opcional y no forma parte de los entregables de las tres semanas. Si el equipo lo elige como su mejora acotada, pide al agente que programe un comando que indique qué falta para ejecutar Lambda. No lo sumes como requisito adicional.

**Mensaje al agente:**

```text
Construye tools/doctor.py para diagnosticar este repositorio. Usa preferentemente
la biblioteca estándar de Python y conserva el código existente.

Debe comprobar, sin instalar ni corregir nada automáticamente:
- Sistema operativo, arquitectura y el intérprete que lo está ejecutando.
- Archivos de configuración y datos requeridos, según el código y el README.
- Disponibilidad de los módulos importados por el proyecto. No supongas que
  el nombre de un paquete en pip coincide siempre con su nombre de importación.
- Disponibilidad de Docker y de Compose si esta configuración los requiere.
- Para los servicios, informa por separado si un puerto responde y si se
  comprobó la respuesta de la aplicación. Puerto abierto no equivale a salud.

Resuelve rutas desde la ubicación del proyecto, no solo desde el directorio
actual. Usa tiempos de espera acotados. No leas ni imprimas valores secretos.
Muestra resultado y acción sugerida por comprobación. Explica qué pruebas
no pudiste hacer y no declares que toda la aplicación está sana.

Añade --json para producir un resumen procesable y documenta los códigos
de salida que decidas usar. Revisa el diff y ejecuta una prueba del diagnóstico.
No generes fallos borrando archivos: usa un directorio temporal o simulación
para comprobar al menos un caso de prerrequisito ausente.
```

El nombre `tools/doctor.py` es el archivo que construirán en esta actividad, no una herramienta que ya venga en el repositorio original. Si el agente propone otra ubicación por las convenciones de tu copia, actualiza los comandos siguientes.

**Terminal — después de revisar la implementación y usando el intérprete del proyecto:**

```bash
python tools/doctor.py
python tools/doctor.py --json
```

Si tu entorno usa `python3` o una ruta explícita al entorno virtual, utiliza esa forma. Comprueba qué intérprete ejecutas con:

```bash
python -c "import sys; print(sys.executable); print(sys.version)"
```

**Qué revisar:** el diagnóstico debe decir qué comprobó realmente. “No se pudo consultar Docker” y “Docker no está instalado” son conclusiones distintas. El JSON debe corresponder con la salida legible. Si el diagnóstico no puede comprobar algo, lo correcto es conservar ese límite.

**Resultado:** ya tienes una herramienta propia que otro equipo puede ejecutar antes de pedir ayuda.

---

## 5. Usa el agente para resolver los problemas de tu sistema operativo

Trabaja con un problema real o con los ajustes que ya hicieron en clase. Puede estar relacionado con rutas, entorno virtual, imports, dependencias, permisos, puertos, arquitectura del procesador, interfaz gráfica o conexión con servicios.

### Si el problema sigue ocurriendo

**Mensaje al agente — reemplaza los corchetes con tus datos:**

```text
Ayúdame a resolver este problema de ejecución.

Acción que intenté: [acción].
Comando y directorio: [comando exacto y directorio].
Entorno confirmado: [SO, CPU, shell, intérprete, Docker/WSL si corresponde].
Salida observada: [fragmento del error o ruta del log].
Resultado que esperaba: [resultado].

Relaciona el error con el código y la configuración. No asumas que la causa
es el sistema operativo. Usa doctor.py si aporta información. Primero explica
la hipótesis y la comprobación mínima; luego aplica un ajuste pequeño dentro
del repositorio o del entorno virtual del proyecto si la evidencia lo permite.

Conserva mis cambios. No reinstales todas las dependencias ni cambies versiones
masivamente. Si la solución requiere una decisión de tecnología o un cambio
global del sistema, explícala antes de continuar.

Repite el comando que fallaba y una comprobación del comportamiento que
podríamos afectar. Documenta lo observado en
docs/laboratorio_llm/PORTABILIDAD.md.
```

### Si ya lo habías arreglado

```text
El sistema ya funciona, pero tuvimos que modificar [archivos o configuración].
Revisa el diff disponible y estos antecedentes: [descripción o evidencias].
Reconstruye qué problema resolvió cada cambio. Distingue hechos comprobados
de hipótesis retrospectivas; no inventes el error original.

Verifica el estado actual sin revertir el arreglo. Documenta cómo otra persona
puede aplicar la solución y qué convendría incorporar al repositorio.
Si editamos una dependencia instalada, registra paquete, versión, archivo y
parche. Propón una forma reproducible de mantenerlo o una alternativa.
```

### Qué debe generar el agente en PORTABILIDAD.md

| Parte | Contenido útil |
|---|---|
| Entorno | SO y versión, CPU, shell, intérprete y forma de ejecutar servicios. |
| Problema | Acción, comando, error y resultado esperado. |
| Diagnóstico | Causa confirmada o hipótesis, con su fundamento. |
| Ajuste | Archivo/configuración cambiada, motivo y diff o commit. |
| Comprobación | Comando repetido, resultado observado y limitación. |
| Transferencia | Cómo aplica el arreglo otra persona y cómo se revierte. |
| Compatibilidad | Combinaciones probadas y combinaciones no probadas. |

**Si PowerShell bloquea la activación del entorno virtual:** pide al agente que compruebe si puede invocar directamente el ejecutable de Python del entorno. No es necesario comenzar desactivando restricciones globales. **Si aparecen problemas con la GUI:** pide que distinga errores de Tkinter/interfaz de problemas del pipeline y pruebe los componentes por terminal cuando corresponda.

**Si no tienes errores:** solicita un procedimiento de arranque desde una terminal nueva y haz que otra persona lo siga. Detectar un requisito no documentado o mejorar un mensaje de diagnóstico también aporta valor. No es necesario fabricar un fallo ni tener tres sistemas operativos.

**Resultado:** un ajuste comprobado y transferible, o una ejecución reproducible con sus límites explícitos.

---

## 6. Recurso opcional: crea un laboratorio pequeño de datos

Una forma de entender una arquitectura es controlar la entrada y predecir la salida. Vas a comprobar el procesamiento batch con datos sintéticos cuyo resultado conoces. Esta prueba evalúa agregaciones, no la precisión clínica del modelo de anomalías.

### Datos de referencia

Usa los campos que confirme la versión actual del batch. En la versión revisada hay agregaciones por `patient_id` sobre `ecg_value`.

| Paciente sintético | Valores de entrada | Conteo esperado | Media esperada | Mínimo esperado | Máximo esperado |
|---|---|---:|---:|---:|---:|
| PRUEBA-A | 1, 2, 3 | 3 | 2 | 1 | 3 |
| PRUEBA-B | 4, 6 | 2 | 5 | 4 | 6 |

Estos números son **resultados esperados calculados sobre la entrada**, no mediciones de tu ejecución. El agente deberá comparar la salida real con ellos.

**Mensaje al agente:**

```text
Quiero una prueba reproducible del batch con cinco registros sintéticos:
PRUEBA-A tiene valores 1, 2, 3; PRUEBA-B tiene 4, 6.
Los resultados de referencia son: A cuenta 3, media 2, mínimo 1, máximo 3;
B cuenta 2, media 5, mínimo 4, máximo 6.

1. Revisa batch/batch_daily_processor.py y confirma el contrato de entrada.
2. Crea los datos y una prueba bajo tests/ o la carpeta de pruebas existente.
3. Usa una carpeta temporal como data lake y una base de prueba independiente
   si necesitas persistencia. No escribas sobre las tablas/datos del ejercicio.
4. Si no hay una base de prueba disponible, aísla la función de agregación
   con un refactor mínimo y prueba esa unidad con la misma lógica que usa
   el batch. No copies el algoritmo en la prueba para compararlo consigo mismo.
5. Define y ejecuta el comando de prueba. Añade una tolerancia numérica
   razonada para flotantes si hace falta. Registra salida y alcance.
6. Genera docs/laboratorio_llm/PRUEBAS.md con entrada, resultado esperado,
   observado, comando, entorno y límites.

Si necesitas elegir entre prueba unitaria e integración, explica qué podremos
afirmar con cada una y usa la opción ejecutable en nuestro entorno.
```

**Tu siguiente intervención:** revisa la prueba y pídele una segunda entrada. Por ejemplo, un paciente con una sola muestra de valor cero. Antes de ejecutarla, tú debes poder anticipar conteo, media, mínimo y máximo.

```text
Agrega PRUEBA-C con una única muestra de valor 0 como caso independiente.
El resultado esperado es conteo 1, media 0, mínimo 0 y máximo 0.
Ejecuta la prueba y explica por qué comprobar un caso de tamaño uno aporta
información distinta. No concluyas que Kafka o la API funcionan a partir de
esta prueba del cálculo batch.
```

**Resultado:** una prueba que puedes ejecutar de nuevo y que protege un comportamiento concreto. Si solamente comprobaste la agregación, registra ese alcance. La persistencia, la mensajería y la consulta requieren sus propias verificaciones.

---

## 7. Diseña una mejora y elige algo que quieras construir

Con el sistema explorado, pide alternativas y toma una decisión. La propuesta debe ser pequeña y demostrable dentro del tiempo disponible. Puede atender una necesidad funcional, de portabilidad, configuración, pruebas, observabilidad o documentación ejecutable.

Antes de elegir, define qué límites arquitectónicos deben conservarse: responsabilidades de las capas, interfaces o formatos existentes, flujos batch y rápido, persistencia, mecanismos de configuración y despliegue que la mejora no debe alterar. No se presupone que todos estos elementos estén presentes: el equipo los confirma en su versión.

La propuesta debe señalar: problema observado, evidencia, componente responsable, cambio mínimo, elementos que no se tocarán, efecto esperado en las vistas estática/física/dinámica, pruebas de aceptación y riesgo de regresión. Si no puedes explicar cómo comprobar que la mejora preserva los contratos relevantes, reduce su alcance.

**Mensaje al agente:**

```text
Lee el código actual y nuestros documentos de arquitectura, portabilidad y
pruebas. Propón tres mejoras pertinentes para esta implementación.
Para cada una explica: problema observado, usuario o actividad beneficiada,
atributo de calidad, archivos afectados, alternativa más simple, dificultad
estimada y una forma de demostrar el resultado.

Recomienda una para una práctica acotada y señala qué decisión necesitas
del equipo. En esta respuesta analiza y propone; todavía no implementes.
```

Puedes elegir una propuesta del agente o uno de estos retos. Revisa primero si tu versión ya lo resuelve; en ese caso prueba el comportamiento y elige otra mejora útil.

### Reto A. Un simulador que puedas controlar

**Idea:** controlar paciente, cantidad de muestras y frecuencia desde terminal. Servirá para crear demos y pruebas repetibles sin editar el archivo en cada ocasión.

```text
Implementa una mejora pequeña en data_sources/sensor_simulador.py:
aceptar --patient-id, --max-samples y --interval-seconds por argumentos.
Conserva el comportamiento actual cuando no se proporcionen opciones.

Valida los valores; el envío acotado debe terminar y liberar recursos.
Distingue muestras intentadas de envíos confirmados y reporta fallos.
Agrega pruebas del parseo y del límite de muestras usando un productor falso
cuando Kafka no esté disponible. Si realizas una demo con Kafka, usa un tópico
de prueba configurable y evita contaminar el flujo habitual.

Documenta dos comandos de ejemplo y verifica cuáles ejecutaste realmente.
No agregues anomalías artificiales ni cambies el modelo de ML en este reto.
```

**Aceptación:** se pueden ejecutar dos pacientes distintos sin editar código; un límite solicitado detiene el proceso; un argumento inválido produce una explicación clara. Una prueba con productor falso no demuestra entrega a Kafka: registra la diferencia.

### Reto B. Ejecutar sin depender de la carpeta actual

**Idea:** convertir un problema frecuente de rutas en una mejora de portabilidad.

```text
Inspecciona cómo se resuelven rutas de datos, modelos y scripts. Elige un
caso concreto que dependa del directorio desde el que se lanza el programa.
Propón y aplica una resolución portable basada en la raíz del proyecto o
en configuración explícita. Conserva la semántica prevista de los archivos.

Prueba ese caso desde la raíz y desde otra carpeta. No cambies todas las
rutas del proyecto indiscriminadamente. Si hay escrituras, utiliza un destino
temporal para comprobarlas. Documenta configuración y alcance de la solución.
```

**Aceptación:** ambos puntos de entrada resuelven el recurso esperado y las escrituras no aparecen accidentalmente en otra carpeta. Si no existe el problema en tu versión, elige un reto distinto.

### Reto C. Una API que explique su estado

**Idea:** distinguir una aplicación viva de una aplicación lista para atender las consultas del ejercicio.

```text
Diseña e implementa en serving/query_api.py una comprobación de estado
acotada. Separa vivacidad del proceso y disponibilidad para atender la función
que declares. Define qué dependencia y qué recurso necesita esa función.

Comprueba con timeout la condición necesaria y devuelve un estado claro,
con código HTTP coherente cuando no esté disponible. No reveles credenciales
ni errores internos completos. Conserva las rutas existentes.

Prueba dependencia disponible y dependencia no disponible mediante dobles
de prueba si hace falta. Aclara qué condiciones no comprueba este endpoint.
```

**Aceptación:** el caso de indisponibilidad no se presenta como éxito; la consulta termina en un tiempo acotado y el documento describe qué significa el estado. Un puerto abierto no basta para definir disponibilidad funcional.

### Reto D. Una demo visual que ayude a entender Lambda

**Idea:** mejorar la interfaz existente o crear una vista mínima que distinga datos batch, datos recientes y estados sin datos.

```text
Revisa el launcher, las consultas disponibles y los recursos visuales existentes.
Propón la modificación más pequeña para que una persona pueda distinguir
qué está observando de batch y qué de la capa rápida. Usa datos reales de la
API o de la fuente existente; si necesitas datos simulados, identifícalos.

Implementa la opción elegida con controles etiquetados, estado sin datos,
mensaje de error y descripción textual. Reutiliza el stack existente cuando
sea suficiente. No inventes métricas ni muestres una garantía clínica.
Comprueba la pantalla en ejecución y documenta la fuente de cada indicador.
```

**Aceptación:** el usuario distingue las fuentes y puede reconocer un error o ausencia de datos. Una captura demuestra la presentación; las consultas deben verificarse por separado.

### Registra la decisión sin llenar otro formulario extenso

Después de elegir, envía:

```text
Genera docs/laboratorio_llm/PROPUESTA.md con problema y evidencia,
atributo de calidad, dos alternativas, elección del equipo y consecuencias.
Define un escenario con fuente, estímulo, entorno, elemento afectado,
respuesta y medida de respuesta. Añade alcance y exclusiones, archivos previstos,
interfaces o contratos que deben conservarse y criterios de aceptación
verificables. Explica el impacto previsto por vista: estática, física y dinámica.
Distingue el diseño propuesto de lo que ya está implementado. La opción que
elegimos es [opción] por [razón confirmada por el equipo].
```

Luego autoriza el alcance concreto del reto elegido. Revisa el diff y la comprobación al terminar. No necesitas implementar la propuesta completa si excede la práctica.

---

## 8. Pide una segunda revisión y convierte lo hecho en documentación

### Revisión del cambio

Puedes abrir una conversación nueva con el mismo agente para revisar desde otro contexto. Esto ayuda a formular una revisión separada, pero no la convierte en una verificación independiente ni garantiza encontrar todos los errores.

**Mensaje de revisión:**

```text
Actúa como revisor del cambio actual. Lee AGENTS.md, el contexto, la propuesta
y el diff respecto del punto de control [commit o descripción exacta].
No modifiques código en esta etapa.

Busca defectos concretos, casos límite, regresiones de compatibilidad y pruebas
que no demuestren lo que afirman. Para cada hallazgo indica archivo, escenario,
efecto y cómo comprobarlo. Prioriza problemas funcionales; evita una lista de
preferencias de estilo. Si no encuentras un fallo concreto, dilo.
```

El equipo decide qué hallazgos requieren cambios. Si acepta uno, vuelve a la sesión de implementación, solicita el ajuste y repite la prueba pertinente.

### Documentación generada desde el trabajo real

**Mensaje al agente:**

```text
Actualiza la documentación a partir del código, cambios y pruebas existentes.
No redactes mediciones ni ejecuciones que no ocurrieron.

1. Actualiza ARQUITECTURA.md si cambiaron responsabilidades o conexiones.
2. Actualiza PORTABILIDAD.md con los ajustes y entornos realmente probados.
3. Completa PRUEBAS.md con comandos, esperado, observado y limitaciones.
4. Actualiza PROPUESTA.md: qué se implementó, qué se verificó y qué falta.
5. Crea docs/laboratorio_llm/INICIO_RAPIDO.md para que otro estudiante pueda
   preparar el entorno y ejecutar una demo. Incluye orden, directorio, terminal,
   variables de ejemplo sin secretos, señal de éxito y forma de detenerla.
6. Crea docs/laboratorio_llm/ENTREGA.md con un resumen breve y enlaces a
   esos documentos, al código y a las pruebas.
7. Copia `plantillas/REPORTE_INDIVIDUAL.md` a `docs/laboratorio_llm/REPORTE_INDIVIDUAL.md` y completa un reporte por estudiante.
   Cada reporte debe explicar las tres vistas finales, la mejora, las pruebas,
   la coherencia entre diagramas y la participación individual confirmada por
   su autor. No inventes contribuciones, aprendizajes ni mediciones.

Revisa enlaces y coherencia de estados. Conserva pendientes explícitos.
```

**Prueba final útil:** otra persona sigue `INICIO_RAPIDO.md` sin que le dictes los pasos. Anoten dónde tuvo dudas y pidan al agente que mejore esas instrucciones. Puede ser otro integrante; no necesita otro sistema operativo.

### Guarda un punto de control

En la terminal, revisa antes de seleccionar archivos:

```bash
git status --short
git diff --stat
git diff
```

Usa el panel de control de código fuente del editor o comandos Git para preparar **los archivos que revisaste** y crear un commit. No agregues todo automáticamente si hay datos, secretos o archivos generados. Pide al agente un mensaje de commit que describa el cambio real. Publicar en tu fork es un paso separado.

### Deja el proyecto listo para la siguiente sesión

```text
Actualiza CONTEXTO.md con la versión evaluada, comandos confirmados,
decisiones, pruebas ejecutadas, limitaciones y siguiente tarea concreta.
Mantén el documento breve. Elimina información superada solo cuando quede
claro qué la reemplaza. No copies toda nuestra conversación.
```

**Resultado:** una nueva sesión puede continuar leyendo archivos del repositorio. El conocimiento importante queda disponible junto al código. Las plantillas `AVANCE_SABADO.md` y `REPORTE_INDIVIDUAL.md` sirven como entregables de esta práctica; no llenes formatos adicionales salvo que sean necesarios para documentar la mejora.

---

## 9. Cómo dirigir al agente cuando la respuesta no te sirve

| Situación | Intervención que puedes usar |
|---|---|
| Se queda explicando y no crea el archivo. | “La tarea autoriza crear este archivo en el proyecto. Escríbelo y dime dónde lo guardaste”. |
| Cambia muchos archivos sin relación. | “Acota el trabajo a este problema. Identifica los cambios ajenos y propón cómo separarlos sin perder trabajo”. |
| Afirma que probó sin mostrar ejecución. | “Indica el comando, salida y entorno. Si no lo ejecutaste, corrige el estado y prepara una prueba ejecutable”. |
| Propone reinstalar todo. | “Delimita primero la causa y una comprobación mínima. Conserva las versiones que ya funcionan salvo evidencia”. |
| Una solución funciona solo en su entorno. | “Compara tu entorno con el mío: SO, CPU, shell, intérprete, rutas, servicios y permisos”. |
| Su prueba solo reproduce su implementación. | “Usa una entrada con resultado calculable de manera independiente y explica qué defecto detectaría”. |
| El diagrama agrega componentes inexistentes. | “Relaciona cada componente y flecha con código o configuración; elimina o etiqueta lo que solo sea propuesta”. |
| La conversación se volvió demasiado larga. | “Actualiza CONTEXTO.md con decisiones y pendientes; continuaremos en una sesión nueva”. |

Un prompt útil contiene **objetivo, contexto, alcance y comprobación**. No necesitas un párrafo enorme si esos cuatro elementos están claros.

## 10. Entrega y demostración

Entrega el repositorio o un paquete con el código cambiado y la documentación del laboratorio. El punto de entrada individual es `docs/laboratorio_llm/REPORTE_INDIVIDUAL.md`; la propuesta y las instrucciones comunes pueden compartirse, pero cada estudiante entrega su propio reporte y verifica su contenido.

En una explicación breve muestra:

1. Las vistas estática, física y dinámica de la versión final, y dónde se reflejan en el código/configuración.
2. La mejora, su necesidad y las responsabilidades o contratos que se cuidaron.
3. Una prueba o comprobación con comando, resultado observado y entorno.
4. Un efecto del cambio en cada vista, o una explicación de por qué alguna vista no cambió.
5. Una limitación o riesgo que sigue abierto y una decisión propia que puedas justificar.

El LLM puede haber generado código y documentación. Debes poder verificar el diff, localizar los elementos del diagrama, explicar los resultados reales y defender la decisión de alcance. No se pide estimar qué porcentaje del código escribió la IA.

## Orientación breve para la docente

La actividad evaluable está ajustada a tres semanas del grupo semiescolarizado. El primer sábado se revisa un avance de comprensión y propuesta, no una implementación terminada. La semana 2 se dedica al cambio pequeño y sus pruebas; la semana 3, a cerrar la mejora y producir reportes individuales con las tres vistas finales. Diagnóstico automático y laboratorio de datos son recursos opcionales; no se suman a la carga obligatoria.

Los equipos pueden compartir una mejora implementada, pero cada estudiante debe generar y comprender su reporte individual. Se recomienda evaluar la evidencia, la coherencia entre vistas, las pruebas y la capacidad de explicar decisiones, no el volumen de código ni el número de prompts. Los ajustes por sistema operativo son una posible propuesta cuando existe un problema reproducible. Los prompts describen resultados y condiciones; el alumnado verifica el contenido generado.

El código de referencia se inspeccionó estáticamente en el commit `a2ca3352d23c54177fd803e36bf2fa8d7bb72abf`; este manual no certifica que el sistema se haya ejecutado en todos los entornos. Pedir al agente que confirme los archivos y contratos de la versión del equipo antes de intervenir.

## Fuentes de configuración del agente

Consultadas el 10 de noviembre de 2026. Los nombres de controles y la disponibilidad pueden cambiar; seguir la documentación oficial si la interfaz difiere.

- [Codex en el IDE](https://learn.chatgpt.com/docs/codex/ide): instalación y apertura del panel.
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli): instalación y uso desde una carpeta de proyecto.
- [Autenticación](https://learn.chatgpt.com/docs/auth): inicio de sesión y acceso por API.
- [Instrucciones con AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): alcance y descubrimiento de instrucciones.
- [Permisos del agente](https://learn.chatgpt.com/docs/agent-approvals-security): lectura, escritura y ejecución.
- [Codex Cloud](https://learn.chatgpt.com/docs/cloud): trabajo en entornos remotos.
- [Repositorio Lambda de la asignatura](https://github.com/jrruiz68/lambda-architecture/tree/a2ca3352d23c54177fd803e36bf2fa8d7bb72abf): versión de referencia para preparar los ejercicios.
