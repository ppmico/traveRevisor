<script>
  import { trkSegs, formStep, dataSent, callApi } from "../sharedSht";
  import { Select, Button, GradientButton, Progressbar } from 'flowbite-svelte';
  import SegDisplay from "./SegDisplay.svelte";

  let idTipoCamino = $state('');

  let tiposCamino = [
    { value: "0", name: 'Pista' },
    { value: "1", name: 'Senderos' },
    { value: "2", name: 'Malos caminos' }
  ];

  let segPoints = $derived($trkSegs[$formStep-1]); 
  
  let trkPoints = $trkSegs.map(seg => seg); //quick way to get a [] with every point of every segment

  function handleForward() {
      if (idTipoCamino == '') {
          alert('Por favor, selecciona un tipo de camino');
          return;
      }
      
      const prevIDs = $dataSent.idsTiposCamino;
      $dataSent = {...$dataSent, idsTiposCamino: prevIDs.concat(idTipoCamino)};

      if ($formStep+1 <= trkPoints.length) { //$formStep starts at 1
          $formStep += 1;
      } else {
          $callApi = true; //cambio de pagina
      }
  }

  function handleBackward() {
      if ($dataSent.idsTiposCamino.length == $formStep) {
          //si se ha escogido un tipo de camino para el segmento actual, se elimina
          const prevIDs = $dataSent.idsTiposCamino;
          $dataSent = {...$dataSent, idsTiposCamino: prevIDs.slice(0, -1)};         
      }
      $formStep -= 1;
  }

</script>



<div class="flex-col space-y-9 p-4">
  <h1 class="text-4xl font-extrabold">¿Cómo es el camino durante la ruta?</h1>

  <div class="w-full flex-col space-y-2">
    <div class="flex justify-center"><Progressbar class="w-5/6" progress={100*$formStep/$trkSegs.length}/></div>

    <SegDisplay {trkPoints} {segPoints} />
  </div>
  <div class="flex-col sm:w-full lg:w-[448px]">
    <p class="text-lg font-bold">Indica el tipo de camino del segmento resaltado</p>
    <p class="text-sm font-medium">Escoge la opción que mejor lo describa</p>
    <Select class="mt-2 w-1/3" items={tiposCamino} bind:value={idTipoCamino} placeholder="Escoge un tipo.." />
  </div>

  <div class="flex flex-row space-x-1">
    <Button on:click={handleBackward} class="text-base">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
      </svg>
      Atrás
    </Button>

    {#if $formStep == $trkSegs.length} <!--Botón en el último segmento que cambia para enviar el formulario-->
      <GradientButton on:click={handleForward} shadow color="purple" class="text-base">
        Enviar
        <span class="ml-2">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M12 5l7 7-7 7" />
          </svg>
        </span>
      </GradientButton>
  
    {:else}
      <Button on:click={handleForward} class="text-base">
        Alante
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
      </Button>
    {/if}
  </div>

</div>

