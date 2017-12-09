$(document).ready(function(){
    var homeBox = new google.maps.places.SearchBox(document.querySelector("#id_home"));
    var destinationBox = new google.maps.places.SearchBox(document.querySelector("#id_destination"));
    var user_id=$('#user_id').text()
    $('form').submit(function(event){
        event.preventDefault()
        var locale = destinationBox.getPlaces()[0];
        var locale2 = homeBox.getPlaces()[0]
        qwerty={'home_lat':locale.geometry.location.lat(),'home_lng':locale.geometry.location.lng(),'dest_lat':locale2.geometry.location.lat(),'dest_lng':locale2.geometry.location.lng(),'user_id':user_id}
        console.log(qwerty)
        $.ajax({
            'url':'/passenger/ajax/locale/',
            'type':'POST',
            'data':qwerty,
            'dataType':'json',
            'success': function(data){
              alert(data['success'])
            },
          })
    })
})