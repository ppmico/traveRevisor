<script>
    import { dataSent, trkSegs } from '../sharedSht';
    import GPX from 'gpx-parser-builder';
    import { Dropzone } from 'flowbite-svelte';
  
  
    let nomFile = '';
  
    function handleFileList(fileList) {
      if (fileList.length > 1) {
        alert('Por favor, sube solo un archivo');
      } else {
        const file = fileList[0];
        if (file.name.endsWith('.gpx')) {
          nomFile = fileList[0].name;
          parseGPX(file); // OJOCUIDAO. El parseo del GPX NO es sincrono, pq hay que leer el archivo que es asincrono
        } else {
            alert('Porfavor sube un archivo .GPX');
        }
      }
    }
  
    const dropHandle = (event) => {
      event.preventDefault();
      if (event.dataTransfer.files) {
        const fileList = event.dataTransfer.files;
        handleFileList(fileList);
      }
    };
  
    const handleChange = (event) => {
      if (event.target.files.length > 0) {
        handleFileList(event.target.files);
      }
    };
  
  
    // //Funcion que parsea el gpx y almacena en $dataSent el archivo subido y en $trkSegs todos los segmentos del gpx
    async function parseGPX(file) {

        try {
            const gpxText = await file.text(); //await porque file.text() es async 
            const gpx = GPX.parse(gpxText);
  
            //Comprobaciones del gpx
            if (!gpx.trk || gpx.trk.length == 0) { throw new Error('Error procesando el GPX, por favor sube un gpx válido'); }
            if (gpx.trk.length > 1) { alert('Cuidado¡! Parece que el gpx tiene varios tracks. Se procesarán todos como si fuese el mismo'); }
              
            //Solo si es un gpx valido se actualiza el objeto $dataSent
            $dataSent = { ...$dataSent, file: file }; //updated like this to trigger reactivity
  
            //Se obtiene del objeto GPX el array de segmentos de todos los tracks combinados. cada segmento queda como un array de puntos ([lat,lon])
            let segmentos = [];
            gpx.trk.forEach(trk => {
                segmentos = segmentos.concat(trk.trkseg.map(trkseg => trkseg.trkpt.map(trkpt => [trkpt.$.lat, trkpt.$.lon])))
            });
            $trkSegs = segmentos;
            
        } catch (e) {
            alert(e.message);
        }
  
    }
  
  </script>
  
<Dropzone class="w-1/3 h-32 p-3"
  id="dropzone"
  on:drop={dropHandle}
  on:dragover={(event) => {
    event.preventDefault();
  }}
  on:change={handleChange}>
  <svg aria-hidden="true" class="w-10 h-10 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" /></svg>
  {#if nomFile === ''}
    <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click para subir el archivo .gpx</span> o arrastra y suéltalo</p>
    <p class="text-xs text-gray-500 dark:text-gray-400">Sólo admitidos archivos GPX (MAX. 5 Mb)</p>
  {:else}
    <p>Archivo seleccionado: {nomFile}</p>
  {/if}
</Dropzone>