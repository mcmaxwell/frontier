$('.toggle-menu').click(function () {
  $('<div class="fake-header"></div>').css('height', $('.header').outerHeight()).prependTo('.home-top')
  $(this).toggleClass('active')
  $('.header .main-nav').toggleClass('active')
  $('.header').toggleClass('active')
  if (!$(this).hasClass('active')) {
    $('.fake-header').remove()
  }

  return false
})

$("#menu").on("click", "a", function (event) {
    event.preventDefault();
    var id  = $(this).attr('href'),
      top = $(id).offset().top

    $('body,html').animate({scrollTop: top}, 1500)
  });
