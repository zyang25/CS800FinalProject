/*jslint indent: 4 */
/*global ClassFoo, ClassBar, someFunction */ 

$(document).ready(function(){
       $("#sign_up_submit").click(function(event){
           if($('#nav_p1').val() != $('#nav_p2').val()) {
               alert("Password and Confirm Password don't match");
               event.preventDefault();
           }
       });
});