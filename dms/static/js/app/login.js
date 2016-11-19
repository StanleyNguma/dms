/**
 * Created by stan on 11/19/16.
 */

$(document).ready(function () {

    var login_form = $('#login_form');

    login_form
        .formValidation({

            framework: 'bootstrap',
            fields: {
                password: {
                    validators: {
                        notEmpty: {
                            message: 'The Password is required'
                        }
                    }
                },
                email: {
                    validators: {
                        notEmpty: {
                            message: 'The email address is required'
                        },
                        emailAddress: {
                            message: 'The input is not a valid email address'
                        }
                    }
                }
            }

        })
        .on('success.form.fv', function(e) {
            // Prevent form submission
            e.preventDefault();

            var $form = $(e.target),
                fv    = $form.data('formValidation');

            // Use Ajax to submit form data
            $.ajax({
                url: '/auth/',
                type: 'POST',
                data: $form.serialize(),
                success: function( response ) {
                    console.log( response );
                    if( response.status == '00')
                        window.location = '/';
                    else
                        swal('Could not login', response.message);
                },
                error: function (response) {
                    console.log( response );
                    swal( response.status.toString(), " An error has occurred")
                    
                }
            });

        });



});