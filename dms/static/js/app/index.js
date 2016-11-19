/**
 * Created by stan on 11/19/16.
 */

$(document).ready(function(){

    Dropzone.options.myAwesomeDropzone = {

            autoProcessQueue: false,
            uploadMultiple: true,
            parallelUploads: 4,
            maxFiles: 4,
            url: '/upload/',

            // Dropzone settings
            init: function() {
                var myDropzone = this;
                this.on("addedfile", function() {

                    e.preventDefault();
                    e.stopPropagation();
                    myDropzone.processQueue();

                });

                this.on("success", function(file, response) {

                    if (response.status === '00') {
                        swal('','<div class="alert alert-success" >' + response.message + '</div>');
                    } else if (response.status === '01') {
                        swal('','<div class="alert alert-danger">' + response.message + ' </div>');
                    }
                });
                this.on("successmultiple", function(files, response) {
                });
                this.on("error", function(files, response) {
                    console.log(response);
                    swal('','An error has occurred');
                });
            }

}

});
