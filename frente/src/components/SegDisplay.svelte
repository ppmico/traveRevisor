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
      let track = L.polyline(trkPoints, {color: 'red'}).addTo(map);
      // zoom the map to the track
      map.fitBounds(track.getBounds());
      

    });
    $effect(() => { // every time segPoints changes the previous (if exists) segment is removed and a new one is drawn
      if (seg) seg.removeFrom(map); // remove the previous segment, if it exists
      seg = L.polyline(segPoints, {color: 'green'}).addTo(map);
    });

  </script>
  
  <style>
    #map {
      height: 400px;
      width: 100%;
    }
  </style>
  
  <div id="map"></div>