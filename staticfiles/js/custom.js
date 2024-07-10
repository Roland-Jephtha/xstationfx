// jQuery Initialization
jQuery(document).ready(function($) {
    "use strict";

    setTimeout(function() {
        $('#header-logo').addClass('pix-loaded');
    }, 1300);
    $(".form_type_item").click(function() {
        $(this).toggleClass("item_is_active");
        var panel = $(this).attr('data-pix-toggle');
        $('.' + panel).toggleClass("pix_is_active");
        return false;
    });

    $(".button-collapse").sideNav();
    //$('.modal').modal();
    $('.modal').modal({
        dismissible: true, // Modal can be dismissed by clicking outside of the modal
        opacity: .5, // Opacity of modal background
        inDuration: 300, // Transition in duration
        outDuration: 200, // Transition out duration
        startingTop: '4%', // Starting top style attribute
        endingTop: '10%', // Ending top style attribute
        ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.

            console.log(modal, trigger);
        },
        complete: function() {} // Callback for Modal close
    });

    $('.dropdown-button').dropdown({
        inDuration: 300,
        outDuration: 225,
        constrainWidth: false, // Does not change width of dropdown to that of the activator
        hover: false, // Activate on hover
        gutter: 0, // Spacing from edge
        belowOrigin: true, // Displays dropdown below the button
        alignment: 'left', // Displays dropdown with edge aligned to the left of button
        stopPropagation: false // Stops event propagation
    });

    $('ul.tabs').tabs();

    $(".dropdown-button").dropdown();

    $('select').material_select();

    $('body').on('click', '.pix_noti_close', function() {
        $(this).closest('.pix_notification').fadeOut(500, function() {
            $(this).remove();
        });
    });

    $('#ftp_publish').click(function() {
        if ($('#ftp_host').val() && $('#ftp_username').val() && $('#ftp_password').val()) {
            $.confirm({
                title: 'Publishing Project...',
                boxWidth: '600px',
                useBootstrap: false,
                theme: 'pix-default-modal',
                backgroundDismiss: true,
                content: 'Important: please don\'t close the page while publishing the project!<br><div class="progress">\n' +
                    '      <div class="indeterminate"></div>\n' +
                    '  </div> ' +
                    'This process may take a few minutes.',
                buttons: {
                    cancel: {
                        text: 'HIDE',
                        btnClass: 'btn-cancel',
                    }
                }
            });
        }
    });

    $('.contact_us').click(function(e) {
        e.preventDefault();
        Intercom('showMessages');
        return false;
    });

    $('#delete-project-btn').click(function() {
        $.confirm({
            title: 'DELETE PROJECT',
            boxWidth: '600px',
            useBootstrap: false,
            theme: 'pix-danger-modal',
            backgroundDismiss: true,
            content: 'Are you sure you want to delete the project?',
            buttons: {
                cancel: {
                    text: 'CANCEL',
                    btnClass: 'btn-cancel',
                },
                showpreview: {
                    text: 'DELETE',
                    btnClass: 'btn-red',
                    keys: ['enter', 'shift'],
                    action: function() {
                        window.open('delete_project.html', "_self");
                    }
                }
            }
        });
    });
    if (typeof AOS !== 'undefined') {
        AOS.init({
            easing: 'ease-in-out-sine',
            duration: '1000',
            once: true
        });
    }

});