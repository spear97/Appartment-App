// Function to redirect to a URL
function redirectTo(url) {
  window.location.href = url;
}

function getCity(address) {
  // Define a regular expression to match the city between the first and second commas
  const cityRegex = /,\s*(.*?),/;

  // Return the located City
  return address.match(cityRegex)[1];
}

function getState(address) {
  // Define a regular expression to match the state abbreviation
  const stateRegex = /\b(?:AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)\b/gi;

  // Return the located State
  return address.match(stateRegex)[0];
}

function getZip(address) {
  // Regular expression to match zip code pattern
  var zipRegex = /\b\d{5}(?:-\d{4})?\b/;

  // Return the located ZipCode
  return address.match(zipRegex)[0];
}

function generateTile(img_src, name, min_price, max_price, city_name, state_name, zip_code, link) {
  return {
    imageSrc: img_src,
    title: name,
    min: min_price,
    max: max_price,
    city: city_name + "," + state_name + " " + zip_code,
    url: link,
  }
}

// Function to generate room HTML
function generateRoomHTML(room) {
  return `
    <div class="w3-row w3-center" style="transform: translate(33%, 0%)">
      <div class="w3-third w3-margin-bottom">
        <img src="" alt="${room.title}" style="width:100%">
        <div class="w3-container w3-white">
          <h3>${room.title}</h3>
          <h6 class="w3-opacity">Price Range: $${room.min} - $${room.max}</h6>
          <p>${room.city}</p>
          <button class="w3-button w3-block w3-black w3-margin-bottom" onclick="redirectTo('${room.url}')">Get More Info</button>
        </div>
      </div>
    </div>
  `;
}

function generateTiles() {
  var apts = [];
  for (var i = 0; i < names.length; i++) {
    var tile = generateTile(imgs[i], names[i], mins[i], maxs[i], getCity(addresses[i]), getState(addresses[i]), getZip(addresses[i]), links[i]);
    apts.push(tile);
  }
  return apts;
}

var apts = generateTiles();

// Generate room HTML and append to container
const container = document.getElementById('aptContainer');
apts.forEach(apt => {
  const aptHTML = generateRoomHTML(apt);
  container.innerHTML += aptHTML;
});
