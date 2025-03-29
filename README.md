# TraveRevisor

# TraveRevisor

TraveRevisor es una herramienta diseñada para evaluar rutas como actividad para grupos de tiempo libre. Concretamente, está pensada para ser utilizada por los responsables de grupos scout preparando las rutas para sus educandos, pero perfectamente puede ser usada en casos de uso análogos. 
Permite analizar archivos GPX que contengan la ruta a analizar para determinar si esa travesía es adecuada para diferentes ramas (Castores, Lobatos, Tropa, Escultas o Clan) según criterios como distancia, desnivel y tiempo estimado. La evaluación de la ruta determinará si esta es aceptable según la experiencia de un grupo scout que realiza travesías todos los veranos (Entaban 612) y si es aceptable según el [MIDE](https://montanasegura.com/el-mide/), método que se utiliza para evaluar travesías 
Esta es una herramienta extra qu de que las rutas sean apropiadas para la rama que las va a realizar.
## Características

### Backend (FastAPI)
- **Procesamiento de Archivos GPX**: El backend procesa archivos GPX para calcular:
  - Distancia total de cada segmento.
  - Ascenso y descenso acumulados.
- **Evaluación de Segmentos**: Cada segmento se evalúa según:
  - Tiempo requerido para recorrer el segmento (tiempo MIDE y tiempo real).
  - Adecuación para diferentes grupos (e.g., Castores, Lobatos, Tropa, etc.) según criterios predefinidos.
- **Endpoint API**: Un endpoint de FastAPI (`/query-gpx/`) está disponible para cargar archivos GPX y recibir los resultados de la evaluación en formato JSON.

### Frontend (Astro + Svelte)
- **Formulario Interactivo**: 
  - Carga de archivos GPX.
  - Selección del tipo de grupo (e.g., Castores, Lobatos, etc.).
  - Especificación de si los participantes llevarán mochila grande.
- **Selección de Tipo de Segmento**: Después de cargar un archivo GPX, los usuarios pueden especificar el tipo de camino (e.g., Pista, Sendero, Malos caminos) para cada segmento.
- **Visualización de Resultados**: 
  - Evaluación general de la ruta.
  - Evaluación detallada de cada segmento, incluyendo distancia, ascenso, descenso y adecuación.
  - Los resultados se muestran en un formato de acordeón para facilitar la navegación.
- **Visualización en Mapa**: Se muestra un mapa para visualizar la ruta general y resaltar los segmentos individuales.

### Manejo de Archivos GPX
- **Validación de Archivos**: Asegura que el archivo cargado sea un archivo GPX válido.
- **División de Segmentos**: Soporta rutas divididas en segmentos para una evaluación más precisa.
- **Reducción de Tamaño de Archivos**: Proporciona orientación para reducir el tamaño del archivo GPX si excede el límite.

### Guía para Usuarios
- **Página de Preguntas Frecuentes (FAQ)**: Incluye instrucciones detalladas sobre:
  - Crear y editar archivos GPX usando [gpx.studio](https://gpx.studio).
  - Dividir rutas en segmentos.
  - Reducir el tamaño de los archivos GPX.

## Estructura del Proyecto

### Backend (`espalda/`)
- **`main.py`**: Aplicación FastAPI con el endpoint `/query-gpx/`.
- **`gpx_process.py`**: Maneja el procesamiento de archivos GPX y los cálculos de segmentos.
- **`global_data.py`**: Almacena constantes globales y criterios para la evaluación.
- **`interfaz.py`**: Proporciona lógica adicional para el procesamiento de archivos GPX.
- **`gui.py`**: Una interfaz gráfica básica para uso local (basada en Tkinter).

### Frontend (`frente/`)
- **Framework Astro**: Utilizado para renderizado del lado del servidor y generación de sitios estáticos.
- **Componentes Svelte**:
  - `FormGeneral.svelte`: Maneja el formulario inicial para cargar archivos y seleccionar detalles del grupo.
  - `FormSegmento.svelte`: Permite a los usuarios especificar el tipo de camino para cada segmento.
  - `RezDisplay.svelte`: Muestra los resultados de la evaluación.
  - `SegDisplay.svelte`: Visualiza la ruta y los segmentos en un mapa.
- **Estado Compartido**: Usa `nanostores` para gestionar el estado compartido entre componentes.

### Configuración
- **`astro.config.mjs`**: Configura Astro con integraciones de Svelte y TailwindCSS.
- **`tailwind.config.mjs`**: Configuración de TailwindCSS para estilos.
- **`.env`**: Contiene variables de entorno, como la URL del endpoint de la API.

### Otros
- **`frente/src/pages/faq.md`**: Archivo Markdown para la página de preguntas frecuentes.
- **`frente/src/sharedSht.ts`**: Gestión de estado compartido usando `nanostores`.

## Cómo Ejecutar

### Backend
1. Navega al directorio `espalda/`.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
