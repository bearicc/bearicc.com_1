$(document).ready(function () {
  // dynamic settings
  if($("body").height() < $("html").height()) {
    $("html, body").css({"height": "100%"});
  }
  set_footer_art();

  // event
  $(window).resize(function () {
    set_footer_art();
  });
});

function set_footer_art() {
    var footer_height = $("footer").height();
    $(".main-container").css({"padding-bottom": footer_height+20});
}
