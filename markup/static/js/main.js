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
  //
  // $('.load-more').click(function () {
  //   $.ajax({
  //     url: "",
  //     method: "POST",
  //     data: data,
  //     dataType: "html"
  //   })
  //     .beforeSend(function () {
  //       $('.load-more').addClass('loader')
  //     })
  //     .done(function( data ) {
  //       setTimeout(function (data) {
  //         $('.load-more').removeClass('loader')
  //         $('.news-grid').append(data)
  //       }, 300)
  //     })
  //     .fail(function (xhr, ajaxOptions, thrownError){
  //       if(xhr.status==404) {
  //         $('.load-more').hide()
  //       }
  //     })
  // })
})
