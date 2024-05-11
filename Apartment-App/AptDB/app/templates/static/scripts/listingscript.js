// Function to redirect to a URL
function redirectTo(url) {
  // This function redirects the user to the specified URL by setting the window location
  window.location.href = url;
}

function getCity(address) {
  // This function extracts the city name from the given address using a regular expression
  // Define a regular expression to match the city between the first and second commas
  const cityRegex = /,\s*(.*?),/;
  // Return the located City
  return address.match(cityRegex)[1];
}

function getState(address) {
  // This function extracts the state abbreviation from the given address using a regular expression
  // Define a regular expression to match the state abbreviation
  const stateRegex = /\b(?:AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)\b/gi;
  // Return the located State
  return address.match(stateRegex)[0];
}

function getZip(address) {
  // This function extracts the zip code from the given address using a regular expression
  // Regular expression to match zip code pattern
  var zipRegex = /\b\d{5}(?:-\d{4})?\b/;
  // Return the located ZipCode
  return address.match(zipRegex)[0];
}

function generateTile(img_src, name, min_price, max_price, city_name, state_name, zip_code, link, phone_number) {
  // This function generates a tile object with the provided data
  return {
    imageSrc: img_src, // URL of the image
    title: name, // Name/title of the room
    min: min_price, // Minimum price
    max: max_price, // Maximum price
    city: city_name + "," + state_name + " " + zip_code, // City, state, and zip code combined
    url: link, // URL for more information
    phone_number: phone_number, // The phone number for the apartment
  }
}

// Function to generate room HTML
function generateRoomHTML(room) {
  // This function generates HTML markup for a room tile based on the provided room object
  return `
    <div class="w3-row w3-center" style="transform: translate(33%, 0%)">
      <div class="w3-third w3-margin-bottom">
        <img src="${room.imageSrc}" alt="${room.title}" style="width:100%"> <!-- Image -->
        <div class="w3-container w3-white">
          <h3>${room.title}</h3> <!-- Title -->
          <h6 class="w3-opacity">Price Range: $${room.min} - $${room.max}</h6> <!-- Price Range -->
          <p>City:</p>
          <p><u>${room.city}</u></p> <!-- City, state, and zip code -->
          <br>
          <p>Phone Number:</p>
          <p><u>${room.phone_number}</u></p> <!-- City, state, and zip code -->
          <button class="w3-button w3-block w3-blue w3-margin-bottom" onclick="redirectTo('${room.url}')">Get More Info</button> <!-- Button to get more information -->
        </div>
      </div>
    </div>
  `;
}

function generateTiles() {
  // This function generates room tiles based on the provided data arrays
  var apts = [];
  for (var i = 0; i < names.length; i++) {
    // Generate a tile object for each room and push it to the 'apts' array
    var tile = generateTile(imgs[i], names[i], mins[i], maxs[i], getCity(addresses[i]), getState(addresses[i]), getZip(addresses[i]), links[i], numbers[i]);
    apts.push(tile);
  }
  return apts; // Return the array of room tiles
}

// Generate room tiles and append to container
var apts = generateTiles(); // Generate room tiles
const container = document.getElementById('aptContainer'); // Get container element
apts.forEach(apt => {
  const aptHTML = generateRoomHTML(apt); // Generate HTML markup for each room
  container.innerHTML += aptHTML; // Append HTML markup to container
});
