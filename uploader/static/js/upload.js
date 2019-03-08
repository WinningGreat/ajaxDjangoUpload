/*$(document).ready(function(){

 (function($){
        function processForm( e ){
            $.ajax({
                url: '',
                type: 'post',
                data: $(this).serialize(),
                success: function( data, textStatus, jQxhr ){
                    for (var i = 0;i < data.file_names.length;i++){
            $("#num_upload").append(data.file_names[i])
                },
                error: function( jqXhr, textStatus, errorThrown ){
                    console.log( errorThrown );
                }
            });

            e.preventDefault();
        }

        $('#upload_form').submit( processForm );
    })(jQuery);
/*$("#upload_form").on('submit',(function(e){
        e.preventDefault();
       $.post({
            url: '/upload/',
            data:new FormData(this),
            success: function(data){
            for (var i = 0;i < data.file_names.length;i++){
            $("#num_upload").append(data.file_names[i])



                }
            }

       });*/


       /*$.get({
            url: '/upload/',
            data:{
                'upload_check': true
            },
            success: function(data){
            $("#myBar").width(data.percentage + '%')

            }


       })

}));
        });
*/
$(document).ready(function(){
files_ob = document.getElementById("myFile")
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
$("#upload_form").submit(function(e){
     e.preventDefault();
     var data = new FormData();

var request = new XMLHttpRequest();

// File selected by the user
// In case of multiple files append each of them
for (j=0;j<files_ob.files.length;j++){
data.append("myFile", files_ob.files[j]);
}

// AJAX request finished
request.addEventListener('load', function(e) {
	// request.response will hold the response from the server
	console.log(request.response);
});

// Upload progress on request.upload
request.upload.addEventListener('progress', function(e) {
	var percent_complete = (e.loaded / e.total)*100;
    $("#myBar").width(percent_complete.toString()+'%')
	// Percentage of upload completed
	console.log(percent_complete);
});

// If server is sending a JSON response then set JSON response type
request.responseType = 'json';
// Send POST request to the server side script
request.open('post', 'http://127.0.0.1:8000/upload/');
request.setRequestHeader("X-CSRFToken", csrftoken);
console.log(csrftoken)
request.send(data);

  });


files_ob.addEventListener('change', function() {
	// This is the file user has chosen
	var files = []
	var file_names_str = ""
	for (var i = 0;i<this.files.length;i++){
	files.push(this.files[i])
	file_names_str = file_names_str + "\n" + this.files[i].name
	}

	// Allowed types
	/*var mime_types = [ 'image/jpeg', 'image/png' ];

	// Validate MIME type
	if(mime_types.indexOf(file.type) == -1) {
		alert('Error : Incorrect file type');
		return;
	}*/

	// Max 2 Mb allowed


	// Validation is successful
	// This is the name of the file

	alert('You have chosen the files ' + file_names_str);
});

});