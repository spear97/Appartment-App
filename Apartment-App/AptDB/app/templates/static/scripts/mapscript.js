var coords = coordsData;
var names = namesData;
var addresses = addressData;

var initpoint = coords[0];

// Initialize the map
var mymap = L.map('mapid').setView(initpoint, 13);

// Add a tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

for(let i = 0; i < coords.length; i++)
{
    if (names[i] == undefined) continue;

    var marker = L.marker(coords[i]).addTo(mymap);
    marker.bindPopup("<b><u>"+ names[i] +"</u></b><br>" + "<b>" + addresses[i] + "</b>").openPopup();
}