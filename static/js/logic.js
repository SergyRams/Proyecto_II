// Create the tile layer that will be the background of our map
var map_layer = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "light-v10",
  accessToken: API_KEY
});

var map = L.map("map-id", {
  center: [23.9, -102.66],
  layers: [map_layer],
  zoom: 6
});

map_layer.addTo(map)

// Initialize all of the LayerGroups we'll be using
var layers = {
  PRD: new L.LayerGroup(),
  PAN: new L.LayerGroup(),
  PRI: new L.LayerGroup(),
  Verde: new L.LayerGroup(),
  MORENA: new L.LayerGroup(),
  PT: new L.LayerGroup(),
  Otro: new L.LayerGroup()
};

// //Create the map with our layers
// var map = L.map("map-id", {
//   center: [23.9, -102.66],
//   zoom: 6,
//   layers: [
//     layers.map_layer,
//     layers.PRD,
//     layers.PAN,
//     layers.PRI,
//     layers.Verde,
//     layers.MORENA,
//     layers.PT,
//     layers.Otro
//   ]
// });

// map_layer.addTo(map)

// Create an overlays object to add to the layer control
var overlays = {
  "PRD": layers.PRD,
  "PAN": layers.PAN,
  "PRI": layers.PRI,
  "Verde": layers.Verde,
  "MORENA": layers.MORENA,
  "PT": layers.PT,
  "Otro": layers.Otro
};

// Create a control for our layers, add our overlay layers to it
L.control.layers(null, overlays).addTo(map);

// Create a legend to display information about our map
var info = L.control({
  position: "bottomright"
});

// When the layer control is added, insert a div with the class of "legend"
info.onAdd = function() {
  var div = L.DomUtil.create("div", "legend");
  return div;
};
// Add the info legend to the map
info.addTo(map);

// Initialize an object containing icons for each layer group
var icons = {
  PRD: L.ExtraMarkers.icon({
    markerColor: "yellow",
    shape: "star"
  }),
  PAN: L.ExtraMarkers.icon({
    markerColor: "blue",
    shape: "circle"
  }),
  PRI: L.ExtraMarkers.icon({
    markerColor: "green",
    shape: "circle"
  }),
  Verde: L.ExtraMarkers.icon({
    markerColor: "green",
    shape: "square"
  }),
  MORENA: L.ExtraMarkers.icon({
    markerColor: "red",
    shape: "circle"
  }),
  PT: L.ExtraMarkers.icon({
    markerColor: "red",
    shape: "star"
  }),
  Otro: L.ExtraMarkers.icon({
    markerColor: "white",
    shape: "circle"
  })
};



// call the json file
d3.json(`/api/votos/2018`, function(resultados) {


  // Create an object to keep of the number of states won per presidential party
  // var Votos_partidos = {
  //   PRD: 0,
  //   PAN: 0,
  //   PRI: 0,
  //   Verde: 0,
  //   MORENA: 0,
  //   PT: 0,
  //   Otro: 0
  // };

  // // Initialize partido to access appropriate layers
  // var partido;

  // Loop through the states (they're the same size and have partially matching data)
  resultados.forEach(d => {
    
    // Create a new marker with the appropriate icon and coordinates
    var newMarker = L.marker([d.latitud, d.longitud], {
      // icon: icons[partido]
    });

    // Add the new marker to the appropriate layer
    // newMarker.addTo(layers[partido]);
    newMarker.addTo(map)

    // Bind a popup to the marker that will  display on click. This will be rendered as HTML
    // newMarker.bindPopup(station.name + "<br> Capacity: " + station.capacity + "<br>" + station.num_bikes_available + " Bikes Available");
  });

  // Call the updateLegend function, which will... update the legend!
  // updateLegend(GanadorEstado, Votos_partidos);
});


// Update the legend's innerHTML with the last updated time and station count
function updateLegend(time, Votos_partidos) {
  document.querySelector(".legend").innerHTML = [
    "<p> Partidos con su cantidad de votos a nivel nacional </p>",
    "<p class='out-of-order'>PRI " + Votos_partidos.PRI + "</p>",
    "<p class='coming-soon'>PAN " + Votos_partidos.PAN +  "</p>",
    "<p class='empty'>PRD " + Votos_partidos.PRD +  "</p>",
    "<p class='low'>Verde " + Votos_partidos.Verde +  "</p>",
    "<p class='healthy'>MORENA " + Votos_partidos.MORENA +  "</p>",
    "<p class='low'>Verde " + Votos_partidos.PT +  "</p>",
    "<p class='healthy'>MORENA " + Votos_partidos.Otro +  "</p>" 
  ].join("")
};
