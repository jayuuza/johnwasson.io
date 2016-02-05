
$(function() {

  "use strict";

  // Initialize shuffle.js
  shuffleme.init();

  // Disable demonstrative links!
  $('a[href="#"]').on('click', function(e){
    e.preventDefault();
  });

  // Back to top
  $('#scroll-up').on( 'click', function() {
    $('html, body').animate({scrollTop : 0}, 900);
    return false;
  });

  // Smoothscroll to anchor
  $('a[href^="#"]:not([href="#"])').on('click', function(){
    var id = $(this).attr('href');
    if ($(id).size() > 0) {
      $('html, body').animate({scrollTop: $(id).offset().top}, 500);
    }
    return false;
  });

  // Equal height for grid view
  $('.features.name-only > li, .demos > li').matchHeight();

  // Introduction video
  $('[data-pe-videoid]').prettyEmbed({ useFitVids: true });

  // Add a .body-scrolled to body, when page scrolled
  $(window).on('scroll', function() {
    if ($(document).scrollTop() > 0) {
      $('body').addClass('body-scrolled');
    }
    else {
      $('body').removeClass('body-scrolled');
    }
  });

  // lightSlider
  $(".testimonials, .review-slider .reviews").lightSlider({
    item: 1,
    slideMargin: 10,
    auto: true,
    loop: true,
    pause: 6000,
    pauseOnHover: true,
    adaptiveHeight: true
  });

  //
  // jQuery.countTo
  //
  $(window).on('scroll', function() {
    $('.counter span:not(.counted-before)').each(function(index, value) {
      if (isScrolledIntoView(this)) {
        $(this).countTo().addClass('counted-before');
      }
    });
  });


  //
  // Offcanvas
  //
  $('[data-toggle="offcanvas"]').on('click', function (e) {

    e.preventDefault();

    $('body').toggleClass('offcanvas-show');
    
    if ($('body').hasClass('offcanvas-show')) {
      $('html').css('overflow', 'hidden');
    }
    else {
      $('html').css('overflow', 'visible');
    }
    
  });

  $(window).on('resize', function(){
    if ($(window).width() > 991) {
      $('body').removeClass('offcanvas-show');
      $('html').css('overflow', 'visible');
    }
  });
  

  function isScrolledIntoView(elem) {
    var $elem = $(elem);
    var $window = $(window);

    var docViewTop = $window.scrollTop();
    var docViewBottom = docViewTop + $window.height();

    var elemTop = $elem.offset().top;
    var elemBottom = elemTop + $elem.height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
  }

});

//
// Shuffle.js initialization
//
var shuffleme = (function( $ ) {
  'use strict';

  var $grid = $('.filterable-demo'),
      $filterOptions = $('.filter-demo'),
      $sizer = $grid.find('.shuffle_sizer'),

  init = function() {

    // None of these need to be executed synchronously
    setTimeout(function() {
      listen();
      setupFilters();
    }, 100);

    // instantiate the plugin
    $grid.shuffle({
      itemSelector: 'li',
      delimeter: ',',
      sizer: $sizer    
    });
  },

  // Set up button clicks
  setupFilters = function() {
    var $btns = $filterOptions.children();
    $btns.on('click', function() {
      var $this = $(this),
          isActive = $this.hasClass( 'active' ),
          group = isActive ? 'all' : $this.data('group');

      // Hide current label, show current label in title
      if ( !isActive ) {
        $('.filter-demo .active').removeClass('active');
      }

      $this.toggleClass('active');

      // Filter elements
      $grid.shuffle( 'shuffle', group );
    });

    $btns = null;
  },

  // Re layout shuffle when images load. This is only needed
  // below 768 pixels because the .picture-item height is auto and therefore
  // the height of the picture-item is dependent on the image
  // I recommend using imagesloaded to determine when an image is loaded
  // but that doesn't support IE7
  listen = function() {
    var debouncedLayout = $.throttle( 300, function() {
      $grid.shuffle('update');
    });

    // Get all images inside shuffle
    $grid.find('img').each(function() {
      var proxyImage;

      // Image already loaded
      if ( this.complete && this.naturalWidth !== undefined ) {
        return;
      }

      // If none of the checks above matched, simulate loading on detached element.
      proxyImage = new Image();
      $( proxyImage ).on('load', function() {
        $(this).off('load');
        debouncedLayout();
      });

      proxyImage.src = this.src;
    });

    // Because this method doesn't seem to be perfect.
    setTimeout(function() {
      debouncedLayout();
    }, 500);
  };      

  return {
    init: init
  };
}( jQuery ));