$(document).ready(function(){
    console.log('we are live')
    var searchBox = new google.maps.places.SearchBox(document.querySelector("#id_home"));
    var searchBox2 = new google.maps.places.SearchBox(document.querySelector("#id_destination"));
    
    
    function loadMap() {
        var address = $("#home").text()
        var addressWork = $("#away").text()
        
        var geocoder = new google.maps.Geocoder();        
        
        geocoder.geocode( { 'address': address}, function(results, status) {
            var locati = results[0].geometry.location; 
        });
    
     }
     searchBox.addListener('places_changed', function() {
        var locale = searchBox.getPlaces()[0];
        console.log(locale.geometry.location.lat());
        
    });
    // google.maps.event.addDomListener(window, 'load', loadMap);
    loadMap()
    })