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

function check_email() {
    
    console.log("Checking email.") // sanity check

    // Get cookie then setup ajax
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
    });

    $.ajax({
        url : ".", // the endpoint
        type : "POST", // http method
        data : {
        emailcheck : $('#signup_email').val()
        }, 
        success: function(res, status, xhr) { 
        	if(res=="OK"){
        		console.log("Good");
        		$('#signup-nav').unbind('submit');
        		$('<input/>').attr('type', 'hidden')
          		.attr('name', "signup_submit")
          		.appendTo('#signup-nav');
        		$('#signup-nav').submit();

        	}else{
        		$('#form_email_div').attr('class','form-group has-feedback has-error');
        		$('#signup_email_error').text('Email already exists.');
        		console.log("Email already exists.");
        	}	
  		},
    	error: function (request, status, error) {
        	alert(request.responseText);
   		},
    });
};


function check_password(){
    console.log("Checking password");
    // Get cookie then setup ajax
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
    });

    $.ajax({
        url : ".", // the endpoint
        type : "POST", // http method
        data : {
        email : $('#login_email').val(),
        password: $('#login_password').val(),
        checkpassword_ajax: 1,
        },
        success: function(res, status, xhr) { 
            if(res=="OK"){
                console.log("password ok");
                $('#login-nav').unbind('submit');
                $('<input/>').attr('type','hidden')
                .attr('name','login_submit')
                .appendTo('#login-nav');
                $('#login-nav').submit();

            }else{
                $('#form_password_div').attr('class','form-group has-feedback has-error');
                $('#login_password_error').text('Oops, password is not correct.');
                console.log("Password bad");
            }   
        },
        error: function (request, status, error) {
            alert(request.responseText);
        },
    });

}