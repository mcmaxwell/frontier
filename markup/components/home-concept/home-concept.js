const $slickSlider = $('.js-home-concept__list')
const settings = {
  dots: false,
  arrows: false,
  infinite: false,
  variableWidth: true,
  slidesToShow: 4,
  responsive: [
  {
    breakpoint: 1360,
    settings: {
      slidesToShow: 3
    }
  },
  {
    breakpoint: 1030,
    settings: {
      slidesToShow: 2
    }
  },
  {
    breakpoint: 618,
    settings: {
      slidesToShow: 1
    }
  }
]
}

function initSlider () {
  // if ($(window).width() < 1024) {
    // if (!$slickSlider.hasClass('slick-initialized')) {
      $slickSlider.slick(settings)
    // }
  // } else {
  //   if ($slickSlider.hasClass('slick-initialized')) {
  //     $slickSlider.slick('unslick')
  //   }
  // }
}

initSlider()

// $(window).on('resize', function () {
//   initSlider()
// })
