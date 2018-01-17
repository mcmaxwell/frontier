const $slickSlider = $('.js-home-concept__list')
const settings = {
  dots: false,
  arrows: false,
  infinite: false,
  variableWidth: true
}

function initSlider () {
  if ($(window).width() < 1024) {
    if (!$slickSlider.hasClass('slick-initialized')) {
      $slickSlider.slick(settings)
    }
  } else {
    if ($slickSlider.hasClass('slick-initialized')) {
      $slickSlider.slick('unslick')
    }
  }
}

initSlider()

$(window).on('resize', function () {
  initSlider()
})
