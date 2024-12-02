<!-- src/components/Prueba.svelte -->
<script>
  import SegDisplay from "./SegDisplay.svelte";
  let i = $state(0);
  let trkSegs = [
    [[40.7128, -74.0060], [34.0522, -118.2437], [41.8781, -87.6298]],
    [[41.8781, -87.6298], [29.7604, -95.3698]],
    [[29.7604, -95.3698], [39.7392, -104.9903]]
  ];
  let trkPoints = trkSegs.map(seg => seg);
  let segPoints = $derived(trkSegs[i]);
</script>
  
<SegDisplay {trkPoints} {segPoints} />
<button onclick={() => i -= 1}>Decrement</button>
<button onclick={() => i += 1}>Increment</button>
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
  