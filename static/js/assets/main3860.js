(function ($) {
    "use strict";
    
    jQuery(document).ready(function ($) {

        // Hero carousel (2-second change)
        var hero2Responsive = {
            0: { items: 1 }
        };
        owlCarouselActivate('.hero2-carousel', false, hero2Responsive, 2000, 1000, true, 'fadeOut', 1000, false);

        // Case carousel
        var caseResponsive = {
            0: { items: 1 },
            576: { items: 2 },
            992: { items: 3 },
            1367: { items: 4 },
            1750: { items: 5 }
        };
        owlCarouselActivate('.case-carousel', true, caseResponsive, 5000, 1500, false, false, 1500, true);

        // Testimonial carousel
        var testimonialResponsive = {
            0: { items: 1 },
            992: { items: 2 }
        };
        owlCarouselActivate('.testimonial-carousel', false, testimonialResponsive, 5000, 1500, false, false, 1500, true, 30);

        // Partner carousel
        var partnerResponsive = {
            0: { items: 2 },
            576: { items: 3 },
            992: { items: 5 }
        };
        owlCarouselActivate('.partner-carousel', false, partnerResponsive, 3000, 500, false, false, 1500, true, 30);

        // Owl Carousel activation function
        function owlCarouselActivate(selector, nav, responsive, autoplayTimeout = 5000, autoplaySpeed = 1000, dots = true, animateOut = false, smartSpeed = 1000, autoplayHoverPause = true, margin = 0, loop = true, autoplay = true) {
            var $selector = $(selector);
            if ($selector.length > 0) {
                $selector.owlCarousel({
                    loop: loop,
                    autoplay: autoplay,
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

        // Language dropdown toggle
        $('.language-btn').on('click', function (event) {
            event.preventDefault();
            $(this).next('.language-dropdown').toggleClass('open');
        });

        // Slicknav initialization
        $('#mainMenu').slicknav({ prependTo: '#mobileMenu' });

        // Back to top functionality
        $('.back-to-top').on('click', function () {
            $("html, body").animate({ scrollTop: 0 }, 1000);
        });

        // Isotope for filtering cases
        var $grid = $('.case-lists .cases').isotope({
            layoutMode: 'fitRows',
            itemSelector: '.single-case',
            fitRows: { gutter: '.case-lists .gutter-sizer' }
        });

        $('.case-types').on('click', 'button', function () {
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({ filter: filterValue });
        });

        $('.case-types li button').on('click', function () {
            $('.case-types').find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });

        // Particles effect for home 3
        if ($("#particles-js").length > 0) {
            particlesJS.load('particles-js', 'assets/js/particles.json');
        }

        // Ripple effect for home 4
        if ($("#heroHome4").length > 0) {
            $('#heroHome4').ripples({
                resolution: 500,
                dropRadius: 20,
                perturbance: 0.04
            });
        }

        // Background video for home 5
        if ($("#bgndVideo").length > 0) {
            $("#bgndVideo").YTPlayer();
        }

    });

    $(window).on('scroll', function () {
        // Sticky menu activation
        if ($(window).scrollTop() > 180) {
            $('.header-area').addClass('sticky-navbar');
        } else {
            $('.header-area').removeClass('sticky-navbar');
        }

        // Back to top button visibility
        if ($(window).scrollTop() > 1000) {
            $('.back-to-top').addClass('show');
        } else {
            $('.back-to-top').removeClass('show');
        }
    });

    $(window).on('load', function () {
        // Preloader fadeout on page load
        $(".loader-container").addClass('loader-fadeout');
    });

}(jQuery));
