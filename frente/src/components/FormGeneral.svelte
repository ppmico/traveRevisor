<script>  
    import { dataSent, formStep } from "../sharedSht";
    import FileUpload from "./FileUpload.svelte";
    import { Button, Radio, RadioButton, ButtonGroup } from 'flowbite-svelte';

    let idConMochilon = $state(false);
    let idLaRama = $state(false);

    //funcion que se ejecuta al intentar continuar el formulario
    function handleSubmit(e) {
        e.preventDefault();

        if (!idLaRama) {
          alert('¡No se eligió ninguna rama! Por favor, haz click una rama')
        } else if (!idConMochilon) {
          alert('Por favor, especifica si se llevará mochila de travesía')
        } else if (!$dataSent.file) {
            alert('¡No se subió ningún archivo! Por favor, sube el archivo gpx.');
        } else {
          $dataSent = {...$dataSent, idMochilon: idConMochilon, idRama: idLaRama}; //updated like this to trigger reactivity
          $formStep += 1; //avanza al siguiente paso del formulario
        }
    }

  
</script>

<div class="flex-col space-y-9 p-4">

  <p class="text-4xl font-extrabold">Información básica de la ruta</p>
  <div class="flex sm:flex-col-reverse lg:flex-row space-x-2.5 ">
    <FileUpload />
    <div class="flex-col">
      <p class="text-lg font-bold">Sube el archivo .gpx de la ruta</p>      
      <ul class="text-base list-disc ml-6 font-medium">
        <li>El archivo no puede pesar más de 5 Mb (<span class="text-blue-600 hover:text-blue-800 underline cursor-pointer"><a href="faq#reduce-el-tamaño-de-una-ruta" target="_blank">¿cómo lo reduzco?</a></span>)</li>
        <li>Se recomienda usar la página <span class="text-blue-600 hover:text-blue-800 underline cursor-pointer"><a href="https://gpx.studio/es/app#6.96/42.519/-0.059" target="_blank">gpx.studio</a></span> para crearlo </li>
        <li>Recuerda <span class="font-extrabold"> separar el track en segmentos</span>, para indicar los tipos de camino en la ruta (<span class="text-blue-600 hover:text-blue-800 underline cursor-pointer"><a href="faq#2-divide-la-ruta-en-segmentos" target="_blank">¿y eso como lo hago?</a></span>)</li>
      </ul>
    </div>
  </div>

  <div class="flex-col">
    <p class="text-lg font-bold">¿Qué rama hará la excursión?</p>
    <p class="text-sm font-medium">Escoge una opción</p>

    <ButtonGroup>
      <RadioButton value="0" bind:group={idLaRama}>
        <div class="w-full p-3">
          <div class="font-medium">Castores</div>
          <div class="text-sm font-normal text-gray-500 dark:text-gray-400">(6-8 años)</div>
        </div>
      </RadioButton>
      <RadioButton value="1" bind:group={idLaRama}>
        <div class="w-full p-3">
          <div class="font-medium">Lobatos</div>
          <div class="text-sm font-normal text-gray-500 dark:text-gray-400">(8-11 años)</div>
        </div>
      </RadioButton>
      <RadioButton value="2" bind:group={idLaRama}>
        <div class="w-full p-3">
          <div class="font-medium">Tropa</div>
          <div class="text-sm font-normal text-gray-500 dark:text-gray-400">(11-14 años)</div>
        </div>
      </RadioButton>
      <RadioButton value="3" bind:group={idLaRama}>
        <div class="w-full p-3">
          <div class="font-medium">Escultas</div>
          <div class="text-sm font-normal text-gray-500 dark:text-gray-400">(14-17 años)</div>
        </div>
      </RadioButton>
      <RadioButton value="4" bind:group={idLaRama}>
        <div class="w-full p-3">
          <div class="font-medium">Clan</div>
          <div class="text-sm font-normal text-gray-500 dark:text-gray-400">(17-21 años)</div>
        </div>
      </RadioButton>
    </ButtonGroup>
  </div>


  <div class="flex-col space-y-1 w-64">
    <p class="text-lg font-bold">¿Llevarán mochila de travesía?</p>
    <ul class=" w-full items-center rounded-lg border border-gray-300 sm:flex divide-x rtl:divide-x-reverse divide-gray-300">
      <li class="w-1/2"><Radio value="1" bind:group={idConMochilon} class="p-3">Si</Radio></li>
      <li class="w-1/2"><Radio value="0" bind:group={idConMochilon} class="p-3">No</Radio></li>
    </ul>
  </div>
  <Button on:click={handleSubmit} class="text-base">Continuar</Button>
</div>
