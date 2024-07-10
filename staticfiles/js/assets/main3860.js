(function($) {
    "use strict";
    jQuery(document).ready(function($) {

        // hero carousel
        var hero2Responsive = {
            0: {
                items: 1
            }
        };
        owlCarsouelActivate('.hero2-carousel', false, hero2Responsive, 10000, 1000, true, 'fadeOut', 1000, false);

        // case carousel
        var caseResponsive = {
            0: {
                items: 1
            },
            576: {
                items: 2
            },
            992: {
                items: 3
            },
            1367: {
                items: 4
            },
            1750: {
                items: 5
            }
        };
        owlCarsouelActivate('.case-carousel', true, caseResponsive, 5000, 1500, false, false, 1500, true);

        // testimonial carousel
        var testimonialResponsive = {
            0: {
                items: 1
            },
            992: {
                items: 2
            },
        };
        owlCarsouelActivate('.testimonial-carousel', false, testimonialResponsive, 5000, 1500, false, false, 1500, true, 30);

        // Partner carousel
        var partnerResponsive = {
            0: {
                items: 2
            },
            576: {
                items: 3
            },
            992: {
                items: 5
            },
        };
        owlCarsouelActivate('.partner-carousel', false, partnerResponsive, 3000, 500, false, false, 1500, true, 30);

        //owl carousel activate function 
        function owlCarsouelActivate(selector, nav, responsive, autoplayTimeout, autoplaySpeed, dots, animateOut, smartSpeed, autoplayHoverPause, margin = 0, loop = true, autoplay = true) {
            var $selector = $(selector);
            if ($selector.length > 0) {
                $selector.owlCarousel({
                    loop: loop,
                    autoplay: true,
                    autoplayTimeout: autoplayTimeout,
                    autoplaySpeed: autoplaySpeed,
                    dots: dots,
                    nav: nav,
                    navText: ["<i class='flaticon-left-arrow'></i>", "<i class='flaticon-right-arrow'></i>"],
                    smartSpeed: smartSpeed,
                    autoplayHoverPause: autoplayHoverPause,
                    animateOut: animateOut,
                    margin: margin,
                    responsive: responsive
                });
            }
        }

        // language dropdown toggle on clicking button
        $('.language-btn').on('click', function(event) {
            event.preventDefault();
            $(this).next('.language-dropdown').toggleClass('open');
        });

        // slicknav initialization
        $('#mainMenu').slicknav({
            prependTo: '#mobileMenu'
        });

        // Back to top
        $('.back-to-top').on('click', function() {
            $("html, body").animate({
                scrollTop: 0
            }, 1000);
        });

        // isotope for cases
        var $grid = $('.case-lists .cases').isotope({
            layoutMode: 'fitRows',
            itemSelector: '.single-case',
            fitRows: {
                gutter: '.case-lists .gutter-sizer'
            }
        })

        // bind filter on button click
        $('.case-types').on('click', 'button', function() {
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({
                filter: filterValue
            });
        });

        // change is-checked class on buttons
        $('.case-types li button').on('click', function() {
            $('.case-types').find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });

        // particles effect initialization for home 3
        if ($("#particles-js").length > 0) {
            particlesJS.load('particles-js', 'assets/js/particles.json');
        }

        // ripple effect initialization for home 4
        if ($("#heroHome4").length > 0) {
            $('#heroHome4').ripples({
                resolution: 500,
                dropRadius: 20,
                perturbance: 0.04
            });
        }

        // // background video initialization for home 5
        if ($("#bgndVideo").length > 0) {
            $("#bgndVideo").YTPlayer();
        }

    });


    $(window).on('scroll', function() {
        // sticky menu activation
        if ($(window).scrollTop() > 180) {
            $('.header-area').addClass('sticky-navbar');

        } else {
            $('.header-area').removeClass('sticky-navbar');

        }

        // back to top button fade in / fade out
        if ($(window).scrollTop() > 1000) {
            $('.back-to-top').addClass('show');
        } else {
            $('.back-to-top').removeClass('show');
        }
    });


    jQuery(window).on('load', function() {
        // preloader fadeout onload
        $(".loader-container").addClass('loader-fadeout');
    });

}(jQuery));