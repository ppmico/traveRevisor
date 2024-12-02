<script>
    import { trkSegs, formStep, dataSent } from "../sharedSht";
    import SegDisplay from "./SegDisplay.svelte";

    let idTipoCamino = '';

    let segPoints = $derived($trkSegs[$formStep-1]); 
    
    let trkPoints = $trkSegs.map(seg => seg); //quick way to get a [] with every point of every segment

    function handleForward() {
        if (idTipoCamino == '') {
            alert('Por favor, selecciona un tipo de camino');
            return;
        }
        
        const prevIDs = $dataSent.idsTiposCamino;
        $dataSent = {...$dataSent, idsTiposCamino: prevIDs.concat(idTipoCamino)};

        if ($formStep <= $trkSegs.length) { //$formStep starts at 1
            $formStep += 1;
        } else {
            //TODO: cambiar de pagina y llamar a la API
            console.log($dataSent);
            window.location.href = '/submitRez';
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
<SegDisplay {trkPoints} {segPoints} />

<form>
    
    <label for="rama">Qué tipo camino?</label>
    <select id="rama" required bind:value={idTipoCamino}>
      <option value="0">Pista</option>
      <option value="1">Sendero</option>
      <option value="2">Malos caminos</option>  
    </select>
    <br>    
  
  </form>

<button onclick={handleBackward}>Atras</button>
<button onclick={handleForward}>Alante</button>