import 'components/home-top/home-top'
import 'components/home-news/home-news'
import 'components/header/header'
import 'components/home-map/home-map'
import 'components/home-concept/home-concept'

$(document).ready(function () {
  $(document).foundation()

  /* Every time the window is scrolled ... */
  function showElements () {
    $('.hideme').each( function () {
      let bottomObject = $(this).position().top + 50
      let bottomWindow = $(window).scrollTop() + $(window).height()

      /* If the object is completely visible in the window, fade it it */
      if ( bottomObject < bottomWindow) {
        $(this).addClass('show')
        // $(this).animate({
        //   'opacity': '1',
        //   'transform': 'translate(0)'
        // }, 400)
      } else {
        $(this).removeClass('show')

      }
    })
  }
  showElements()
  $(window).on('scroll', function () {
    showElements()
  })
})
