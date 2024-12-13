<script>
    import FormGeneral from "./FormGeneral.svelte";
    import FormSegmento from "./FormSegmento.svelte";
    import { formStep, callApi } from "../sharedSht";
    import ApiCall from "./ApiCall.svelte";

</script>

{#if !$callApi}
    
    {#if $formStep == 0}
        <FormGeneral />
    {:else}
        <FormSegmento />
    {/if}

{:else}
    <ApiCall/>
{/if}