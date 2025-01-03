<script>
    import "../styles/global.css"
    
    import { dataSent } from '../sharedSht';
    import ApiCall from './ApiCall.svelte';

    $dataSent.file = new File([""], "filename.txt", { type: "text/plain" });
    $dataSent.idRama = "0";
    $dataSent.idMochilon = "0";
    $dataSent.idsTiposCamino = [0,1,0,1];
</script>

<ApiCall/>