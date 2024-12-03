<!-- src/components/Prueba.svelte -->
<script>
  import {dataSent} from '../sharedSht'

  console.log("co1", dataSent.get());


  const fileInput = new File(['../../../gepex.gpx'], 'gepex.gpx', {
    type: 'application/gpx+xml',
  });

  $dataSent = {...$dataSent, idMochilon: 1, idRama: 0, idsTiposCamino: [1,2,0], file: fileInput};
  // dataSent.set({idMochilon: "1", idRama: "0", idsTiposCamino: [1,2,0], file: fileInput});
  console.log("co", dataSent.get());

</script>


<a href="/submitRez">oiiiiiiiiiiiiiiiiiiiii </a>

<!-- cómo hacer api req:
    <script>
      import { dataSent } from '../sharedSht';
      import { paso } from '../sharedSht';
      import { gpxFile } from '../sharedSht';
    </script>

    {#if paso == 2}

    <button on:click={async () => {
      const formData = new FormData();
      formData.append('file', gpxFile);
      formData.append('rama_id', 0);
      [1, 2, 0, 1, 0].forEach((value, index) => {
        formData.append('tipos_camino_id', value.toString());
      });
      formData.append('mochila_id', 0);

      try {
        const response = await fetch('http://127.0.0.1:8000/query-gpx/', {
          method: 'POST',
          body: formData
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(`Error: {errorData.message}, {errorData.error}`);
        }

        const data = await response.json();
        alert('¡Archivo enviado con éxito!');
        console.log(data);
      } catch (error) {
        console.error(error);
        alert('Ocurrió un error.');
      }
    }}> 
      click me
    </button>

    {/if} -->
  