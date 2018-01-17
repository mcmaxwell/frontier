$('.scroll-down').click(function() {
  $("html, body").animate({ scrollTop: $('main').offset().top - 50 }, 600);
  return false;
})
