
function toggleMenu () {
  if(!$('.toggle-menu').hasClass('active')) {
    $('.header .main-nav .menu').animate({
      opacity: 1
    }, 300)
  } else {
    $('.header .main-nav .menu').animate({
      opacity: 0
    }, 300)
  }
  $('.toggle-menu').toggleClass('active')
  $('.header').toggleClass('active')
}

function sctollToEl (el) {

  if (el || location.hash) {
    let top = el ? $(el).offset().top - 120 : $(location.hash).offset().top - 120
    if (top) {
      $('body,html').animate({scrollTop: top}, 500)
      if (el && $(window).width() < 1180) {
        toggleMenu()
      }
    }
  }
}

// if (!$('.fake-header').length) {
//   $('<div class="fake-header"></div>').css('height', $('.header').outerHeight()).insertBefore('.header')
// } else {
//   $('.fake-header').remove()
// }

$('.toggle-menu').click(function () {
  toggleMenu()
  return false
})

if (location.pathname !== '/' && location.pathname !== '/en/') {
  for (let i = 0; i < $('#menu a').length; i++) {
    $('#menu a').eq(i).attr('href', '/' + $('#menu a').eq(i).attr('href'))
  }
} else {
  sctollToEl()
}

$('#menu').on('click', 'a', function () {
  sctollToEl($(this).attr('href'))
  return false
})

if ($(window).scrollTop() < $('.header').outerHeight()) {
  $('.header').addClass('top')
} else {
  $('.header').removeClass('top')
}

// Hide Header on on scroll down
let didScroll
let lastScrollTop = 0
let delta = 5
let navbarHeight = $('.header').outerHeight()

function hasScrolled () {
  let st = $(window).scrollTop()

  // Make sure they scroll more than delta
  if (Math.abs(lastScrollTop - st) <= delta) {
    return
  }

  // If they scrolled down and are past the navbar, add class .nav-up.
  // This is necessary so you never see what is "behind" the navbar.
  if (st < navbarHeight) {
    $('.header').addClass('top')
  } else {
    $('.header').removeClass('top')
  }

  if (st > lastScrollTop && st > 0) {
      // Scroll Down
    $('.header').removeClass('show')
  } else {
      // Scroll Up
    if (st + $(window).height() < $(document).height()) {
      $('.header').addClass('show')
    }
  }

  lastScrollTop = st
}



$(window).scroll(function () {
  didScroll = true
  if ($(window).scrollTop() > 50) {
    $('.scroll-down').addClass('hide')
  } else {
    $('.scroll-down').removeClass('hide')
  }
})

setInterval(function (event) {
  if (didScroll) {
    hasScrolled()
    didScroll = false
  }
}, 30)
