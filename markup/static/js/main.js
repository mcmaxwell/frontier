import 'components/home-top/home-top'
import 'components/home-news/home-news'
import 'components/header/header'

$(document).ready(function () {
  $(document).foundation()

  $('.home-map__toggle').click(function () {
    $(this).hasClass('active') ? $(this).parent().find('img').attr('src', './static/img/assets/home-map/map.jpg') : $(this).parent().find('img').attr('src', './static/img/assets/home-map/map-active.jpg')
    $(this).toggleClass('active')
  })
})
