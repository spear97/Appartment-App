document.addEventListener("DOMContentLoaded", function() {
  // This event listener ensures that the DOM content is fully loaded before executing the script

  // Get the DOM element with id "mapid"
  var mapContainer = document.getElementById('mapid');

  // Create a map instance and set its center and zoom level
  var map = L.map(mapContainer).setView([32.72930399616183, -97.11519679906151], 13);

  // Add a tile layer to the map
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // Loop through the data arrays to add markers to the map
  for(var i = 0; i < namesData.length; i++)
  {
      // Add a marker to the map at the coordinates provided in coordsData array
      var marker = L.marker(coordsData[i]).addTo(map);
      // Create marker text with name and address data
      var markerTxt = "<b>" + namesData[i] + "</b><br>" + addressData[i];
      // Bind a popup to the marker with the marker text
      marker.bindPopup(markerTxt);
  }
});
