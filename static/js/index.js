var bScroll = true;

$(document).ready(function () {
  $('.main-gallery').flickity({
      cellAlign: 'center',
      contain: true,
      cellSelector: '.gallery-cell',
      setGallerySize: false,
      imagesLoaded: true,
      wrapAround: true,
      autoPlay: 2000,
      pageDots: false
  });

  $("#welcome").click(function () {
    $("#left-panel").toggleClass("hover");
  });

  $(".back-to-top").click(function () {
    $("html,body").animate({scrollTop: 0}, 500, "swing");
    return false;
  });

  $(window).scroll(function () {
    scrollHandleNow();

    // ------------------------------------------------------------
    // scrollHandle that can be optimized as executed every certain period
    if(bScroll) {
      scrollHandle();
      // handle scroll every 50
      bScroll = false;
      setTimeout(function () {
        scrollHandle();
        bScroll = true;
      }, 50);
    }
    // ------------------------------------------------------------
  }); // scroll

}); // ready

function scrollHandleNow() {

}

function scrollHandle() {
  height = $(window).scrollTop();
  if (height > 0) {
    $(".back-to-top").show("drop", 500);
  } else {
    $(".back-to-top").hide("drop", 500);
  }
}

function scrollToAnchor(id) {
  var anchor = $(id);
  $("html,body").animate({scrollTop: anchor.offset().top}, 500, "swing");
  setTimeout(function () {
  }, 600);
}
