
function toggleMenu () {
  if(!$('.fake-header').length) {
    $('<div class="fake-header"></div>').css('height', $('.header').outerHeight()).insertBefore('.header')
  } else {
    $('.fake-header').remove()
  }
  $('.toggle-menu').toggleClass('active')
  $('.header .main-nav').toggleClass('active')
  $('.header').toggleClass('active')
  $('.header-clone').toggle()
}

function sctollToEl (el) {
  if (el || location.hash) {
    let top = el ? $(el).offset().top : $(location.hash).offset().top
    if (top) {
      $('body,html').animate({scrollTop: top}, 500)
      if (el && $(window).width() < 1024) {
        toggleMenu()
      }
    }
  }
}

$('.toggle-menu').click(function () {
  toggleMenu()
  return false
})

$('.header')
  .clone(true, true)
  .addClass('header-clone')
  .appendTo('body')
  .on('click', '.menu a', function () {
    sctollToEl($(this).attr('href'))
  })

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


function hasScrolled () {
  let st = $(window).scrollTop()

  // Make sure they scroll more than delta
  if (Math.abs(lastScrollTop - st) <= delta) {
    return
  }


  // If they scrolled down and are past the navbar, add class .nav-up.
  // This is necessary so you never see what is "behind" the navbar.
  if(st < navbarHeight + 100) {
    $('.header-clone').addClass('top')
  } else {
    $('.header-clone').removeClass('top')
  }
  if (st > lastScrollTop && st > navbarHeight || st < navbarHeight + 300) {
      // Scroll Down
      $('.header-clone').removeClass('show')
  } else {
      // Scroll Up
    if (st + $(window).height() < $(document).height()) {
      $('.header-clone').addClass('show')
    }
  }

  lastScrollTop = st
}
