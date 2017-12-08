$(document).ready(function(){
    function loadMap() {
        var address = $("#home").text()
        var addressWork = $("#work").text()
        
        var geocoder = new google.maps.Geocoder();        
        var mapOptions = {
            center:new google.maps.LatLng(49, -77),
            zoom:11
            
        }
        var map = new google.maps.Map(document.getElementById("map-sample"),mapOptions);
        var searchBox = new google.maps.places.SearchBox('nairobi');
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

     }
    google.maps.event.addDomListener(window, 'load', loadMap);


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
