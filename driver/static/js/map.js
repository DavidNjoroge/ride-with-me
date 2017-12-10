$(document).ready(function(){
    function loadMap() {
        var address = $("#home").text()
        var addressWork = $("#work").text()
        
        var geocoder = new google.maps.Geocoder();        
        var mapOptions = {
            center:new google.maps.LatLng(49, -77),
            zoom:11
            
        }
        // var marker = new google.maps.Marker({
        //     position: myLatLng,
        //     map: map,
        //     title: 'Hello World!'
        // });

        var map = new google.maps.Map(document.getElementById("map-sample"),mapOptions);
        // var searchBox = new google.maps.places.SearchBox('nairobi');
        console.log('javascript is loading')
        
        // geocoder.geocode( { 'address': address}, function(results, status) {
        //     var locati = results[0].geometry.location;       
        //     var mapOptions = {
        //         center:new google.maps.LatLng(locati.lat(), locati.lng()),
        //         zoom:11
        //     }
        //     var map = new google.maps.Map(document.getElementById("map-sample"),mapOptions);
        //     var marker = new google.maps.Marker({
        //     position: new google.maps.LatLng(locati.lat(), locati.lng()),
        //     map: map,
        //     });
        //     var marker = new google.maps.Marker({
        //     position: new google.maps.LatLng(locati.lat(), locati.lng()),
        //     map: map,
        //     });
        // });
        var infoWindow = new google.maps.InfoWindow;
        
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
        
            infoWindow.setPosition(pos);
            infoWindow.setContent('Location found.');
            infoWindow.open(map);
            map.setCenter(pos);
            }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
            });
        } else {
            // Browser doesn't support Geolocation
            handleLocationError(false, infoWindow, map.getCenter());
        }
        google.maps.event.addDomListener(window, 'load', loadMap);
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(-1.2682643, 36.81112140000005),
            map: map,
            title: 'Hello World!'
            
        }); 

     }
    loadMap()
    // var marker = new google.maps.Marker({
    //     position: myLatLng,
    //     map: map,
    //     title: 'Hello World!'
    // });
    // var marker = new google.maps.Marker({
    //     position: new google.maps.LatLng(locati.lat(), locati.lng()),
    //     map: map,
    // });
    // function codeAddress() {
    //     var address = $("#work").text()
    //     var addressWork = $("#work").text()
        
    //     console.log(address)
    //     var geocoder = new google.maps.Geocoder();

    //     geocoder.geocode( { 'address': addressWork}, function(results, status) {
    //       var location = results[0].geometry.location;
    //     //   alert('LAT: ' + location.lat() + ' LANG: ' + location.lng());
    //     });
    // }
    // codeAddress()
    

})
