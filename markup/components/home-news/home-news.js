const $slickSlider = $('.js-news-grid')
const settings = {
  dots: true,
  arrows: false,
  infinite: false
}

function initSlider () {
  if ($(window).width() < 768) {
    $('.js-news-grid').after($('.all-news'))
    if (!$slickSlider.hasClass('slick-initialized')) {
      $slickSlider.slick(settings)
    }
  } else {
    if ($slickSlider.hasClass('slick-initialized')) {
      $slickSlider.slick('unslick')
    }
    $('.all-news').appendTo($('.js-news-grid'))
  }
}

initSlider()

$(window).on('resize', function () {
  initSlider()
})
