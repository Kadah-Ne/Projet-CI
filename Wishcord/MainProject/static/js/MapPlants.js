function initMap() {
    var center = {lat: 45.187477, lng: 5.716271};
    var locations = []
    // var locations = [
    //   ['Philz Coffee<br>\
    //   801 S Hope St A, Los Angeles, CA 90017<br>\
    // ',   34.046438, -118.259653],
    // ];
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 9,
      center: center
    });
    var infowindow =  new google.maps.InfoWindow({});
    var marker, count;
    for (count = 0; count < locations.length; count++) {
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[count][1], locations[count][2]),
        map: map,
        title: locations[count][0]
      });google.maps.event.addListener(marker, 'click', (function (marker, count) {
        return function () {
          infowindow.setContent(locations[count][0]);
          infowindow.open(map, marker);
        }
      })(marker, count));
    }
}

function addPoint()
{
    var center = {lat: 45.187477, lng: 5.716271};  
    var locations = JSON.parse(document.getElementById('points').textContent)
    // var locations = [
    //   ['Philz Coffee<br>\
    //   801 S Hope St A, Los Angeles, CA 90017<br>\
    // ',   34.046438, -118.259653],
    // ];
    console.log(locations)
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 9,
        center: center
      });
      var infowindow =  new google.maps.InfoWindow({});
      var marker, count;
      for (count = 0; count < locations.length; count++) {
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(locations[count][1], locations[count][2]),
          map: map,
          title: locations[count][0]
        });google.maps.event.addListener(marker, 'click', (function (marker, count) {
          return function () {
            infowindow.setContent(locations[count][0]);
            infowindow.open(map, marker);
          }
        })(marker, count));
      }
}

