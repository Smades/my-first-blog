/*jslint browser: true*/
/* eslint-env browser */
/*global $*/

$(document).ready(
    function () {
        $('#button').click(
            function () {

                var activity = $('input[name=ListItem]').val();
                var location = $('input[name=place]').val();
                var time = $('input[name=time]').val();

                if (activity.replace(/\s+/g, '') !== '' && location.replace(/\s+/g, '') !== '' && time.replace(/\s+/g, '') !== '') {

                    $('ol').append('<li id="listitem">' + '<p class="activitylist">' + activity + '</p>' + '<span class="timelist">' + time + '</span>' + '<p class="locationlist">' + location + '</p></li>');

                    $('input[name=ListItem], input[name=place], input[name=time], input[name=uname], input[name=psw]').val('');
                }
            });

        $('#loginbutton1').click(
            function () {
                
                var username = $('input[name=uname]').val();
                var password = $('input[name=psw]').val();
                
                if (username.replace(/\s+/g, '') !== '' && password.replace(/\s+/g, '') !== '') {
                    
                console.log(username + password)
                $('#loginyes').remove().fadeOut('slow');
              
                $('#navbar').append('<li class="nav-item nav-link" id="loginyes">Logged in as ' + username + '</li>');
                
                }




            });

        $('#logout1').click(
            function () {

                $('#logout').remove().fadeOut('slow');
                $('#loginyes').remove().fadeOut('slow');




            });




        $("input[name=ListItem], input[name=place], input[name=time]").keydown(function (event) {
            if (event.keyCode == 13) {
                $("#button").click();
                $('input[name=ListItem], input[name=place], input[name=time]').val('');
            }
        });

        $(document).on('dblclick', '#todolistcontainer li', function () {
            $(this).toggleClass('strike').fadeOut('slow');
        });



        $('input').focus(function () {
            $(this).val('');
        });

        

    }
);
