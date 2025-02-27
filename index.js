
mapboxgl.accessToken = 'pk.eyJ1IjoiamVubnVyIiwiYSI6ImNtN2xzZmllNTBiMHoybHNhNmRodXpxNnEifQ.t-a8XKObrSU_fFYlZELPUQ';

// Init the map
const map = new mapboxgl.Map({
    container: 'map',
    center: [10.757933, 59.911491], // Oslo
    zoom: 3
});

map.on("click", (event) => {
  const { lng: clickLng, lat: clickLat } = event.lngLat;

  // Find the hmax value at the nearest lngLat coordinate in maxHmax (maxHmax.js)
  const lng = rountToNearestHalf(clickLng);
  const lat = rountToNearestHalf(clickLat);
  const lngLat = `(${lng},${lat})`;
  const hmaxAtLngLat = maxHmax[lngLat] && `${maxHmax[lngLat].toFixed(2)}m` || "–";

  // Build the marker element to be displayed on the map
  const markerElement = document.createElement("div");
  markerElement.classList.add("marker");
  markerElement.innerHTML = `
    <h2>Longitude: ${clickLng.toFixed(2)} Latitude: ${clickLat.toFixed(2)}</h2>
    <p>Max wave height: <strong>${hmaxAtLngLat}</strong></p>
  `

  // Add the marker to the map
  new mapboxgl.Marker({ element: markerElement })
    .setLngLat([clickLng, clickLat])
    .addTo(map);
})

function rountToNearestHalf(num) {
  return (Math.round(num*2)/2).toFixed(1);
}