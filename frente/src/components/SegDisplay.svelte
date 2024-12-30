<script>
    import { onMount } from 'svelte';
    import L from 'leaflet';
    import 'leaflet/dist/leaflet.css';
  
    let {trkPoints, segPoints} = $props();

    let map, seg;

  
    onMount(() => {
      map = L.map('map').setView([51.505, -0.09], 13); //localizacion default del mapa
  
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);
      // draw the overall track
      let track = L.polyline(trkPoints, {color: 'red', dashArray:'10 5'}).addTo(map);
      // zoom the map to the track
      map.fitBounds(track.getBounds());
      

    });
    $effect(() => { // every time segPoints changes the previous (if exists) segment is removed and a new one is drawn
      if (seg) seg.removeFrom(map); // remove the previous segment, if it exists
      seg = L.polyline(segPoints, {color: '#6d28d9', weight: 8}).addTo(map);
    });

  </script>
  
<div class="rounded-3xl" style="height: 448px; width: 100%" id="map"></div>
