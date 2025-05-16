<p align="center">
  <img src="frente/public/webBanner.png" alt="TraveRevisor Banner" style="max-width: 25%; height: auto;">
</p>

# TraveRevisor

TraveRevisor es una herramienta diseñada para evaluar rutas como actividad para grupos de tiempo libre. Concretamente, está pensada para ser utilizada por los responsables de grupos scout preparando las rutas para sus educandos, pero perfectamente puede ser usada en casos de uso análogos. 


Esta aplicación requiere del archivo *[GPX](https://es.wikipedia.org/wiki/GPX#:~:text=GPX%20(GPS%20Exchange%20Format)%20es%20un%20formato%20de%20datos%20XML%20ligero%20para%20el%20intercambio%20de%20datos%20GPS%20entre%20aplicaciones%20y%20servicios%20web%20en%20Internet.%20Se%20puede%20usar%20para%20describir%20puntos%20de%20paso%20(waypoints)%2C%20rutas%20(routes)%20y%20recorridos%20(tracks).)* que describa la ruta que se desea evaluar.
TraveRevisor analizará la ruta y, después de que el usuario indique algunos detalles más sobre la ruta como las edades de los participantes, determinará si esta es aceptable según la experiencia de un grupo scout que realiza travesías todos los veranos (Entaban 612) y si es aceptable según el [MIDE](https://montanasegura.com/el-mide/), un método que se utiliza para evaluar travesías creado por el Gobierno de Aragón.


**Nota**: Esta herramienta es un *apoyo* a la hora de valorar si una ruta es adecuada. **No sustituye el criterio ni la experiencia de los responsables**, ni otros aspectos importantes para la seguridad y el bienestar de quien vaya a realizar la ruta.

## Aspectos técnicos

### Frontend
La página web y sus funcionalidades han sido desarrolladas con [Astro](https://astro.build/) y con su [integración de Svelte](https://docs.astro.build/en/guides/integrations-guide/svelte/), empleando [Tailwindcss](https://tailwindcss.com/) y [Flowbite Svelte](https://flowbite-svelte.com/) para mejorar la usabilidad, interactividad y aspecto de la página.

Otras tecnologías usadas:
- [Leaflet.js](https://leafletjs.com/) para mostrar las rutas en su contexto
- La librería [`gpx-parser-builder`](https://www.npmjs.com/package/gpx-parser-builder) para trabajar con los archivos gpx en la misma página web.

### Backend
El backend está escrito en Python y desplegado en un contenedor Docker. Se encarga de:
- **Procesamiento de Archivos GPX**: Procesa el archivo GPX con la ruta que se desee evaluar para calcular:
  - Distancia total de cada segmento.
  - Ascenso y descenso acumulados.
  - Tiempo requerido para recorrer ese tramo de ruta.
- **Evaluación de la ruta**: Empleando los criterios de la experiencia y del MIDE se determina si la ruta es apropiada para su relización por el grupo de personas cuyo grupo de edades, entre otros detalles, se solicitan al usuario en el frontend.

Empleando [uvicorn](https://www.uvicorn.org/) y [FastAPI](https://fastapi.tiangolo.com/) este backend ofrece un endpoint de API (`/query-gpx/`) que permite hacer solicitudes en las que se le pasa el archivo `.gpx` al endpoint y se reciben como respuesta los resultados de la evaluación en formato JSON.


### Página de Preguntas Frecuentes (FAQ): 
Empleando la integración de Markdown (`.md`) en Astro se ha creado una página con tutoriales para:
  - Crear, editar rutas y guardarlas en archivos GPX usando [gpx.studio](https://gpx.studio).
  - Dividir rutas creadas en [gpx.studio](https://gpx.studio) en segmentos para su correcto análisis con TraveRevisor.
  - Reducir el tamaño de los archivos GPX.

## Despliegue en local

### Backend
Se puede poner en marcha la API de manera manual:
1. Accede al dicectorio `espalda/`.
2. Instala las dependencias:
  ```bash
  pip install --no-cache-dir -r requirements.txt
  ```

3. Lanza la API con uvicorn:   
  ```bash
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```
Ó ejecutando el contenedor Docker:

  ```bash
  docker build -t trave-revisor-backend . && docker run -p 8000:8000 trave-revisor-backend
  ```

### Frontend
Para lanzar la página web en local es necesario:
1. Acceder al directorio `frente/`
2. Cambiar la dirección del endpoint de la API en archivo `.env`, dejándolo con el siguiente valor:
  ```
  PUBLIC_APIDIR="http://127.0.0.1:8000/query-gpx/"
  ```
3. Construir y lanzar el proyecto Astro con 
  ```
  npm ci && npm run build && npm run preview
  ```
