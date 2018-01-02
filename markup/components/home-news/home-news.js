const $slickSlider = $('.js-news-grid')
const settings = {
  dots: true,
  arrows: false,
  variableWidth: true,
  infinite: false
}

if ($(window).width() < 768) {
  $('.js-news-grid').after($('.all-news'))
  $slickSlider.slick(settings)
}

// reslick only if it's not slick()
$(window).on('resize', function () {
  if ($(window).width() > 768) {
    if ($slickSlider.hasClass('slick-initialized')) {
      $slickSlider.slick('unslick')
    }
    return
  }

  if (!$slickSlider.hasClass('slick-initialized')) {
    $('.js-news-grid .all-news').remove()
    return $slickSlider.slick(settings)
  }
})
