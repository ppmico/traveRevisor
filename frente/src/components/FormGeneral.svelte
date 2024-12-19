<script>  
    import { dataSent, formStep } from "../sharedSht";
    import FileUpload from "./FileUpload.svelte";

    let idConMochilon = '';
    let idLaRama = '';

    //funcion que se ejecuta al intentar continuar el formulario
    function handleSubmit(e) {
        e.preventDefault();

        if (!$dataSent.file) {
            alert('¡No se subió ningún archivo! Por favor, sube el archivo gpx.');
            return;
        }
        $dataSent = {...$dataSent, idMochilon: idConMochilon, idRama: idLaRama}; //updated like this to trigger reactivity
        $formStep += 1; //avanza al siguiente paso del formulario
    }

  
</script>


<form class="font-sans" onsubmit={handleSubmit}>
  <FileUpload />

  <label for="rama">Qué rama?</label>
  <select id="rama" required bind:value={idLaRama}>
    <option value="0">Castores</option>
    <option value="1">Lobatos</option>
    <option value="2">Tropa</option>
    <option value="3">Pios</option>
    <option value="4">Clan</option>

  </select>
  <br>
  <p class="text-green-500">Llevarán mochila grande?</p>
  <input type="radio" id="conMochila" name="mochilaRB" value="1" bind:group={idConMochilon} required>
  <label for="conMochila">Sí</label><br>
  <input type="radio" id="sinMochila" name="mochilaRB" value="0" bind:group={idConMochilon} required>
  <label for="sinMochila">No</label><br>
  <!-- <select id="conMochila" required bind:value={idConMochilon}>
    <option value="1">Si</option>
    <option value="0">No</option>
  </select> -->
  <br>
  
  <button type="submit">Continuar</button>

</form>
