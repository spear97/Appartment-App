function generateTile(img_src, name, min_price, max_price, city_name, zip_code, link) {
    return {
      imageSrc: img_src,
      title: name,
      min: min_price,
      max: max_price,
      city: city_name + ", " + zip_code,
      amenities: ["fa fa-bath", "fa fa-phone", "fa fa-wifi", "fa fa-tv", "fa fa-glass", "fa fa-cutlery"],
      url: link, 
    };
  }

// Function to generate room HTML
function generateRoomHTML(room) {
    let amenitiesHTML = "";
    room.amenities.forEach(amenity => {
      amenitiesHTML += `<i class="${amenity}"></i> `;
    });
  
    return `
      <div class="w3-third w3-margin-bottom">
        <img src="${room.imageSrc}" alt="${room.title}" style="width:100%">
        <div class="w3-container w3-white">
          <h3>${room.title}</h3>
          <h6 class="w3-opacity">From ${room.price}</h6>
          <p>${room.city}</p>
          <p class="w3-large">${amenitiesHTML}</p>
          <button class="w3-button w3-block w3-black w3-margin-bottom" onclick="redirectTo('${room.url}')">Choose Room</button>
        </div>
      </div>
    `;
  }
  
  // Function to redirect to a URL
  function redirectTo(url) {
    window.location.href = url;
  }
  
  // Define room data
  const apts = [
    {
      imageSrc: img_src,
      title: "Single Room",
      price: "$99",
      city: "Fort Worth, TX",
      amenities: ["fa fa-bath", "fa fa-phone", "fa fa-wifi"],
      url: "https://www.google.com",
    },
    {
      imageSrc: img_src,
      title: "Double Room",
      price: "$149",
      city: "Arlington, TX",
      amenities: ["fa fa-bath", "fa fa-phone", "fa fa-wifi", "fa fa-tv"],
      url: "https://www.google.com",
    },
    {
      imageSrc: img_src,
      title: "Deluxe Room",
      price: "$199",
      city: "Grand Prairie, TX",
      amenities: ["fa fa-bath", "fa fa-phone", "fa fa-wifi", "fa fa-tv", "fa fa-glass", "fa fa-cutlery"],
      url: "https://www.google.com",
    }
  ];
  
  // Generate room HTML and append to container
  const container = document.getElementById('aptContainer');
  apts.forEach(apt => {
    const aptHTML = generateRoomHTML(apt);
    container.innerHTML += aptHTML;
  });
