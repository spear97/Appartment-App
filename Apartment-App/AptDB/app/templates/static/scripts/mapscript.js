// Initialize the map
var mymap = L.map('mapid').setView([32.70085307741722, -97.21172616504451], 13);

// Add a tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

for(var i=0; i < coordsData.length; i++)
{
    // Add a marker for the first coordinate
    L.marker(coordsData[i]).addTo(mymap)
        .bindPopup('<b>Name:</b> ' + namesData[i] + '<br><b>Address:</b> ' + addressData[i]);
}
