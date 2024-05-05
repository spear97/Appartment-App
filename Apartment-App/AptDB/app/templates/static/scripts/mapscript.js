/*console.log(namesData);
console.log(addressData);
console.log(coordsData);*/

document.addEventListener("DOMContentLoaded", function() {
    // Get the DOM element with id "mapid"
    var mapContainer = document.getElementById('mapid');
  
    // Create a map instance and set its center and zoom level
    var map = L.map(mapContainer).setView([32.72930399616183, -97.11519679906151], 13);
  
    // Add a tile layer to the map
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    for(var i = 0; i < namesData.length; i++)
    {
        var marker = L.marker(coordsData[i]).addTo(map);
        var markerTxt = "<b>" + namesData[i] + "</b><br>" + addressData[i];
        marker.bindPopup(markerTxt).openPopup();
    }
  
    // Add a marker to the map
    //var marker = L.marker([51.5, -0.09]).addTo(map);
  
    // Add a popup to the marker
    //marker.bindPopup("<b>Hello world!</b><br>This is a Leaflet popup.").openPopup();
  });