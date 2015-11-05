

//Função para inicializar um mapa em uma div com id: map
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -29.713293, lng: -53.716976},
    zoom: 15
  });
}
