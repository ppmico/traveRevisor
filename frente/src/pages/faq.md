---
layout: ../layouts/MdLayout.astro
title: Faq
image: '../assets/images/file.png'

---
# FAQ


## Crea tu ruta

Se recomienda usar [gpx.studio](https://gpx.studio/es/app#5.93/41.578/-2.89), que tiene todas las herramientas que necesitarás para crear y editar rutas. 
En su [página de ayuda](https://gpx.studio/es/help) está todo lo que necesitas saber para utilizarla, pero estos son los **pasos generales**:
### 1. Dibuja el camino  
Primero escoge la opción de '*Correr/Caminar*' en el modo ***Planificar o editar una ruta*** y a continuación haz click en los lugares en el mapa por los que debe pasar la ruta. Puedes arrastrar los '**puntos de anclaje**' para hacer que pase exactamente por donde quieras.  
<figure>
   <img class="mx-auto" src="src/assets/gifs/crear_ruta.gif" alt="Gif: Crear ruta y mover un punto de anclaje">
   <figcaption>Crea tu ruta. Puedes mover los puntos de anclaje</figcaption>
</figure>

### 2. Divide la ruta en segmentos 
Esta parte es opcional pero para conseguir una evaluación más precisa debes dividir tu ruta en **segmentos**, creando un segmento cada vez que el tipo de camino cambie (*Pista, Senderos, Malos caminos*). Tranquilidad, no es necesario ser muy preciso. 

Por ejemplo: si la ruta atraviesa un bosque con malos caminos, crea un segmento desde el inicio hasta el final del bosque más o menos, y así podrás realizar la evaluación indicando que ese tramo es de malos caminos.

1. En el modo ***Recortar o dividir*** escoge la opción de '*Segmentos*' en el desplegable
   <figure>
      <img class="mx-auto" src="src/assets/gifs/seleccionar_recortar.gif" alt="Gif: Crear ruta y mover un punto de anclaje">
      <figcaption>Selecciona 'Recortar o dividir' y asegúrate de que sea en segmentos</figcaption>
   </figure> 
2. Separa la ruta segmento por segmento:  
   - Donde hayas creado puntos de anclaje, verás un icono para separar la ruta en dos segmentos por ese punto.  
   - También puedes hacer clic en cualquier otro punto de la ruta para separar por ahí.
   <figure>
      <img class="mx-auto" src="src/assets/gifs/crear_segmento.gif" alt="Gif: Dividir en segmentos el track">
      <figcaption>Puedes recortar por los puntos de anclaje que ya existan o en otro punto de la ruta haciendo click</figcaption>
   </figure>   

   **Cuidado:** no hay ninguna confirmación visual de que has dividido la ruta al clicar, pero puedes volver al modo '*Planificar o editar una ruta*' y si la ruta ha sido recortada aparecerá un punto de anclaje por donde hayas recortado.

### 3. Descarga tu ruta  
1. Ponle un nombre a tu ruta para encontrarla más fácilmente en tu ordenador (opcional).
<figure>
      <img class="mx-auto" src="src/assets/gifs/cambiar_nombre_track.gif" alt="Gif: Cambiar el nombre del track">
      <figcaption>Cambia el nombre de la ruta para encontrar el archivo fácilmente</figcaption>
</figure>

2. Haz click ***Archivo > Exportar*** y luego selecciona ***Descargar archivo***. Puedes también donar para que puedan mantener la página funcionando :)

<figure>
      <img class="mx-auto" src="src/assets/gifs/descargar_ruta.gif" alt="Gif: Descargar el track">
      <figcaption>Exporta el archivo de la ruta</figcaption>
</figure>

¡Listo! Tu ruta está lista para evaluarla con **TraveRevisor**.  


## Reduce el tamaño de una ruta
Si el archivo .gpx en el que tienes tu ruta guardada es demasiado grande (más de 5Mb) puedes subirlo a [gpx.studio](https://gpx.studio/es/app#5.93/41.578/-2.89) para reducir su tamaño.

1. Sube el archivo a [gpx.studio](https://gpx.studio/es/app#5.93/41.578/-2.89) haciendo click en ***Archivo > Abrir...*** y seleccionando de tu ordenador el archivo extensión `.gpx` de tu ruta. 
<figure>
      <img class="mx-auto" src="src/assets/gifs/abrir_gpx.gif" alt="Gif: Abrir un track de tu ordenador">
      <figcaption>Selecciona 'Abrir' y encuentra tu track entre tus archivos</figcaption>
</figure>

2. Una vez subido tu archivo selecciona la herramienta ***Reducir la cantidad de puntos GPS*** y usa el control deslizante para simplificar la ruta (mayor *Tolerancia* = archivo más pequeño, pero también menos preciso). La idea es reducir la complejidad de la ruta pero sin hacerla demasiado sencilla.
Una vez hayas ajustado con el deslizante la complejidad de la ruta haz click en '*Minimizar*'.
<figure>
      <img class="mx-auto" src="src/assets/gifs/minimizar_gpx.gif" alt="Gif: Seleccionar minimizar y simplificar la ruta">
      <figcaption>Simplifica tu ruta para que ocupe menos</figcaption>
</figure>

3. Por último descarga la ruta: Haz click en ***Archivo > Exportar*** y luego selecciona ***Descargar archivo***. Comprueba que el tamaño del archivo resultante es menor a 5Mb, y si no lo es repite el proceso.
<figure>
      <img class="mx-auto" src="src/assets/gifs/descargar_ruta.gif" alt="Gif: Descargar el track">
      <figcaption>Exporta el archivo reducido de la ruta</figcaption>
</figure>