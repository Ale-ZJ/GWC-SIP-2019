// declaring variables
var map;
var our_location;
var view;

// initialize our variables
function init(){
  our_location = ol.proj.fromLonLat([-122.43,37.63]);

  //constructing a view object
  view = new ol.View({ //"ol" to use the OpenLayers API
    center: our_location,
    zoom: 8
  });

  // constructing a map object
  map = new ol.Map({
    target: 'map', //our target references our map divider
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM() //OSM is a layer in OpenLayer //a layer gives the map like a format (?)
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });
}

//pan the map to our home location
function panHome() {
  view.animate({
    center: our_location, //our "home location"
    duration: 2000 //in ms
  });
}

//Get the user to Panama
function goPanama(){
  view.animate({
    center: ol.proj.fromLonLat([-80.78, 8.54]),
    duration: 2000
  });
}

function makeCountryRequest() {
  //get value from textarea element from maps.html
  var country_name = document.getElementById("countryName").value;

  //check if there is something there
  if (country_name == "") {
    alert("You didnt enter any country!");
    return;
  }
}
//
// console.log("country name: " + country_name); //send the country name inputed to the console to make sure it works
//
// //build Countries API query
// var query = "https://restcountries.eu/rest/v2/name/" + countryName;
// var lon = 0.0;
// var lat = 0.0;





//run init when the window loads //KEEP AT THE BOTTOM OF THE CODE
window.onload = init;
