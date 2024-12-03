<script>
    import { dataSent, trkSegs } from '../sharedSht';
    import GPX from 'gpx-parser-builder';

    //Funcion que parsea el gpx y almacena en $dataSent el archivo subido y en $trkSegs todos los segmentos del gpx
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

    function handleFileUpload(file) {// comprueba si el archivo subido es un GPX
        if (file && file.name.endsWith('.gpx')) {
            parseGPX(file); // OJOCUIDAO. El parseo del GPX NO es sincrono, pq hay que leer el archivo que es asincrono
        } else {
            alert('Please upload a GPX file');
        }
    }
</script>

    
<div role="button" tabindex="0" 
    style="border: 2px dashed #ddd; padding: 20px; text-align: center; position: relative; overflow: hidden;">
    <input 
        type="file" 
        accept=".gpx" 
        onchange={(e)=>{handleFileUpload(e.target.files[0])}} 
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; cursor: pointer;"
    />
    {#if $dataSent.file}
        <p>Uploaded: {$dataSent.file.name}</p>
    {:else}
        <p>Click to upload GPX file</p>
    {/if}
</div>

