$(document).ready(function(){
    console.log('javascript is loading')
    function loadMap() {
        var address = $("#home").text()
        var addressWork = $("#work").text()
        
        var geocoder = new google.maps.Geocoder();        
        
        geocoder.geocode( { 'address': address}, function(results, status) {
            var locati = results[0].geometry.location;       
            var mapOptions = {
                center:new google.maps.LatLng(locati.lat(), locati.lng()),
                zoom:11
            }
            var map = new google.maps.Map(document.getElementById("map-sample"),mapOptions);
            var marker = new google.maps.Marker({
            position: new google.maps.LatLng(locati.lat(), locati.lng()),
            map: map,
            });
            var marker = new google.maps.Marker({
            position: new google.maps.LatLng(locati.lat(), locati.lng()),
            map: map,
            });
        });

     }
    google.maps.event.addDomListener(window, 'load', loadMap);
    loadMap()


    function codeAddress() {
        var address = $("#work").text()
        var addressWork = $("#work").text()
        
        console.log(address)
        var geocoder = new google.maps.Geocoder();

        geocoder.geocode( { 'address': addressWork}, function(results, status) {
          var location = results[0].geometry.location;
        //   alert('LAT: ' + location.lat() + ' LANG: ' + location.lng());
        });
    }
    codeAddress()

})
