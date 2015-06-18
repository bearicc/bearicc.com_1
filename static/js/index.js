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

}); // ready
