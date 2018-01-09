$('.toggle-menu').click(function () {
  $(this).toggleClass('active')
  $('.header .main-nav').toggleClass('active')
  $('.header').toggleClass('active')
  return false
})

$('.fake-header').css('height', $('.header').outerHeight())

function sctollToEl (el) {
  if (el && location.hash) {
    let top = el ? $(el).offset().top : $(location.hash).offset().top
    if (top) {
      $('body,html').animate({scrollTop: top}, 1500)
      if ($(window).width() < 1024) {
        $('.toggle-menu').click()
      }
    }
  }
}

if (location.pathname !== '/') {
  for (let i = 0; i < $('#menu a').length; i++) {
    $('#menu a').eq(i).attr('href', './' + $('#menu a').eq(i).attr('href'))
  }
} else {
  sctollToEl()
}

$('#menu').on('click', 'a', function () {
  sctollToEl($(this).attr('href'))
})
// Hide Header on on scroll down
let didScroll
let lastScrollTop = 0
let delta = 5
let navbarHeight = $('.header').outerHeight()

$(window).scroll(function () {
  didScroll = true
})

setInterval(function (event) {
  if (didScroll) {
    hasScrolled()
    didScroll = false
  }
}, 250)


function hasScrolled () {
  let st = $(window).scrollTop()

  // Make sure they scroll more than delta
  if (Math.abs(lastScrollTop - st) <= delta) {
    return
  }

  // If they scrolled down and are past the navbar, add class .nav-up.
  // This is necessary so you never see what is "behind" the navbar.
  if (st > lastScrollTop && st > navbarHeight) {
      // Scroll Down
      $('.header').css('top', -$('.header').outerHeight())
  } else {
      // Scroll Up
    if (st + $(window).height() < $(document).height()) {
      $('.header').css('top', '')
    }
  }

  lastScrollTop = st
}
