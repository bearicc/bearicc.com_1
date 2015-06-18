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

  $("#resume-link").click(function () {
    $("#content .resume").toggle("drop", 500);
    $("#resume-link i.fa-arrow-right").switchClass("fa-arrow-right", "fa-arrow-down", 500);
    $("#resume-link i.fa-arrow-down").switchClass("fa-arrow-down", "fa-arrow-right", 500);
    $("html,body").toggleClass("footer-down", 500);
    $("footer").toggleClass("footer-down", 500);
  });

}); // ready
