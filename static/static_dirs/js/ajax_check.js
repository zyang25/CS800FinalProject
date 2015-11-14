// $('#signup-nav').on('submit', function(event){
// 	event.preventDefault();
//     console.log("form submitted!")  // sanity check
//     if (check_email()){
//     	$('#signup-nav').submit();
//     }

// });

function email_check_result(){
	if(check_email()){
		return true;
	}else{
		return false;
	}
}

function check_email() {
    
    console.log("Checking...") // sanity check
    
    // Get csrftoken Setup Ajax
	    function getCookie(name) {
	    var cookieValue = null;
		    if (document.cookie && document.cookie != '') {
		        var cookies = document.cookie.split(';');
		        for (var i = 0; i < cookies.length; i++) {
		            var cookie = jQuery.trim(cookies[i]);
		            // Does this cookie string begin with the name we want?
		            if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                break;
		            }
		        }
		    }
	    return cookieValue;
		}
		var csrftoken = getCookie('csrftoken');
		$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
	            // Only send the token to relative URLs i.e. locally.
	            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	        }
	    }
		});
	// Get csrftoken


	console.log(csrftoken) // sanity check

    $.ajax({
        url : ".", // the endpoint
        type : "POST", // http method
        data : {
        emailcheck : $('#signup_email').val()
        }, // data sent with the post request
        success: function(res, status, xhr) { 
        	if(res=="OK"){
        		console.log("Fire");
        		return true;
        	}else{
        		console.log("Bad");
        		return false;
        	}	
  		},
    	error: function (request, status, error) {
        	alert(request.responseText);
   		},
    });
};