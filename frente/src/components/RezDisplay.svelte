<script>
  import "../styles/global.css"
  import { apiResponse } from "../sharedSht";
  import { Accordion, AccordionItem } from 'flowbite-svelte';

  const data = apiResponse.get();
</script>

<div class="max-w-4xl mx-auto p-6 space-y-6">
  <Accordion>
    {#each data.segments as segment (segment.id)}
      <AccordionItem>
        <h3 slot="header" class={
          segment.koticApproved && segment.experienceApproved 
            ? "text-green-600" 
            : "text-red-600"
        }>
          Segmento {segment.id}
        </h3>
        <div class="grid grid-cols-3 gap-4">
          <div>
            <p class="font-medium">Distancia</p>
            <p>{segment.distance.toFixed(2)} km</p>
          </div>
          <div>
            <p class="font-medium">Ascenso</p>
            <p>{segment.totalAscent.toFixed(2)} m</p>
          </div>
          <div>
            <p class="font-medium">Descenso</p>
            <p>{segment.totalDescent.toFixed(2)} m</p>
          </div>
          <div>
            <p class="font-medium">Tiempo MIDE</p>
            <p>{segment.mideTime.toFixed(2)} h</p>
          </div>
          <div>
            <p class="font-medium">Tiempo Real</p>
            <p>{segment.actualTime.toFixed(2)} h</p>
          </div>
          <br/>
          <div>
            <p class="font-medium">Según Kotic</p>
            <p class={segment.koticApproved ? "text-green-600" : "text-red-600"}>
              {segment.koticApproved ? "✓ Aceptable" : "✗ No aceptable"}
            </p>
          </div>
          <div>
            <p class="font-medium">Según Experiencia</p>
            <p class={segment.experienceApproved ? "text-green-600" : "text-red-600"}>
              {segment.experienceApproved ? "✓ Aceptable" : "✗ No aceptable"}
            </p>
          </div>
        </div>
      </AccordionItem>
    {/each}
  </Accordion>

  <div class="bg-gray-100 p-4 rounded-lg mt-6">
    <h2 class="text-xl font-semibold mb-3">Valoración General</h2>
    <div class="space-y-2">
      <p>
        <span class="font-medium">Kotic: </span>
        <span class={data.overall.koticApproved ? "text-green-600" : "text-red-600"}>
          {data.overall.koticApproved ? "✓ Aceptable" : "✗ No aceptable"}
        </span>
      </p>
      <p>
        <span class="font-medium">Experiencia: </span>
        <span class={data.overall.experienceApproved ? "text-green-600" : "text-red-600"}>
          {data.overall.experienceApproved ? "✓ Aceptable" : "✗ No aceptable"}
        </span>
      </p>
    </div>
  </div>
</div>
