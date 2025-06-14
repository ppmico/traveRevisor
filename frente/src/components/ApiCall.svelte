<script>
    import { Spinner } from 'flowbite-svelte';
    import { dataSent, apiResponse } from '../sharedSht';

    const file = $dataSent.file;
    const ramaId = $dataSent.idRama;
    const mochilaId = $dataSent.idMochilon;
    const tiposCaminosId = $dataSent.idsTiposCamino;
    const formData = new FormData();

    if (file) formData.append('file', file);
    if (ramaId) formData.append('rama_id', ramaId);
    if (mochilaId) formData.append('mochila_id', mochilaId);
    if (tiposCaminosId && tiposCaminosId.length > 0) {
        tiposCaminosId.forEach((value) => {
            formData.append('tipos_camino_id', value.toString());
        });
    }

    async function sendData() {
        try {
            const controller = new AbortController(); //para añadir timeout al fetch
            const timeout = setTimeout(() => controller.abort(), 60000);

            const response = await fetch(import.meta.env.PUBLIC_APIDIR, { //TODO: mover url a .env
                method: 'POST',
                body: formData,
                signal: controller.signal 
            }).finally(() => clearTimeout(timeout));

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error('Error: ' + errorData.message + ', ' + errorData.error);
            }
            const data = await response.json();

            // Archivo enviado con éxito
            apiResponse.set(data);
            window.location.href = './eval-results';

        } catch (error) {
            // if (error.name === 'AbortError') then Request timed out'
            console.error(error);
            alert('Ocurrió un error. Intentelo de nuevo');
            window.location.reload();
        }
    }

    sendData();
</script>

<!-- Placeholder que se muestre en pantalla mientras se hace la api call -->
<div class="flex flex-col justify-center items-center h-screen italic"><Spinner/> Enviando datos...</div>
