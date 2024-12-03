<script>
    import { dataSent } from '../sharedSht';

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
            const response = await fetch('http://127.0.0.1:8000/query-gpx/', {
                method: 'POST',
                body: formData
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error('Error: ' + errorData.message + ', ' + errorData.error);
            }
            const data = await response.json();
            
            console.log('Response data:', data);
            alert('¡Archivo enviado con éxito!');
        } catch (error) {
            console.error(error);
            alert('Ocurrió un error.');
        }
    }

    sendData();


</script>