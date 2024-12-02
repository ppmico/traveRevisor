<script>
    import FormGeneral from "./FormGeneral.svelte";
    import FormSegmento from "./FormSegmento.svelte";
    import { formStep } from "../sharedSht";

</script>

{#if $formStep == 0}
    <FormGeneral />
{:else}
    <FormSegmento />
{/if}
