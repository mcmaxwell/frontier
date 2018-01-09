$('.home-map__toggle').click(function () {
  //$(this).hasClass('active') ? $(this).parent().find('img').attr('src', './static/img/assets/home-map/map.jpg') : $(this).parent().find('img').attr('src', './static/img/assets/home-map/map-active.jpg')
  $(this).toggleClass('active')
  $('.home-map').toggleClass('active')
  $('.home-map__item-list').removeClass('active')
  return false
})

$('.home-map__item').click(function () {
  $('.home-map__item-list').removeClass('active')
  $(this).next().toggleClass('active')
  $('.home-map__item').removeClass('active')
  $(this).toggleClass('active')
  return false
})

$('.home-map .close-button').click(function () {
  $('.home-map__item-list').removeClass('active')
  $('.home-map__item').removeClass('active')
  return false
})
