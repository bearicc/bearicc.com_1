var bScroll = true;
var aside_offset_top = $(".aside").offset().top;
var $html = $("html");
var $aside = $(".aside");
var aside_width = $aside.css("width");
var $main= $(".main");

$(document).ready(function () {
  // dynamic settings
  set_footer();

  // event
  $(window).resize(function () {
    set_footer();

    aside_width = $aside.css("width");

    if ($html.width() < 992) {
      $main.css({"position": "",
                 "width": "",
                 "left": "",
                 "top": ""});
      $aside.css({"position": "",
                  "width": "",
                  "left": "",
                  "top": ""});
    }
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
  var height = $(window).scrollTop();
  if (height > 0) {
    $(".back-to-top").show("drop", 500);
  } else {
    $(".back-to-top").hide("drop", 500);
  }
  if ($html.width() >= 992) {
    if (aside_offset_top <= height) {
      $main.css({"position": "relative",
                 "left": $(".main").offset().left-$(".main").parent().offset().left,
                 "top": $(".main").offset().top-$(".main").parent().offset().top});
      $aside.css({"position": "fixed",
                  "width": aside_width,
                  "left": $(".aside").offset().left-$(window).scrollLeft(),
                  "top": 0});
    }
    else {
      $main.css({"position": "relative",
                 "width": "75%",
                 "left": "0",
                 "top": "0"});
      $aside.css({"position": "relative",
                 "width": "25%",
                  "left": "0",
                  "top": "0"});
    }
  } else {

  }
}

function scrollToAnchor(id) {
  var anchor = $(id);
  $("html,body").animate({scrollTop: anchor.offset().top}, 500, "swing");
  setTimeout(function () {
  }, 600);
}

function set_footer() {
  var footer_height = $("footer").height();
  if($("body").height() < $("html").height()) {
    console.log("<");
    $("html, body").css({"height": "100%"});
    $("footer").css({"position": "absolute", "bottom": "0"});
    // $(".main-container").css({"padding-bottom": footer_height+20});
  } else {
    $("html, body").css({"height": ""});
    $("footer").css({"position": "", "bottom": ""});
  }
}
