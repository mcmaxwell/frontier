$('.home-map__toggle').click(function () {
  //$(this).hasClass('active') ? $(this).parent().find('img').attr('src', './static/img/assets/home-map/map.jpg') : $(this).parent().find('img').attr('src', './static/img/assets/home-map/map-active.jpg')
  $(this).toggleClass('active')
  $('.home-map').toggleClass('active')
  $('.home-map__item-list').removeClass('active')
  return false
})

$('.home-map__item').click(function (e) {

  // $('.home-map__item-list').removeClass('active')
  // $('.home-map__item').removeClass('active')
  //
  // if($(this).hasClass('active')) {
  //   $(this).removeClass('active')
  //   $(this).next().removeClass('active')
  // }
  // else {
  //   $(this).addClass('active')
  //   $(this).next().toggleClass('active')
  // }

  return false;
})

$(document).mouseup(function (e){ // событие клика по веб-документу
  var list = $('.home-map__item-list'); // тут указываем ID элемента
  var item = $('.home-map__item');

  if (item.is(e.target) && !$(e.target).hasClass('active')  ) {
    $('.home-map__item-list').removeClass('active')
    $('.home-map__item').removeClass('active')
    $(e.target).toggleClass('active')
     $(e.target).next().toggleClass('active')
  } else if (!list.is(e.target) && list.has(e.target).length === 0) { // и не по его дочерним элементам
    list.removeClass('active'); // скрываем его
    $('.home-map__item').removeClass('active');
  }
});

$('.home-map .close-button').click(function () {
  $('.home-map__item-list').removeClass('active')
  $('.home-map__item').removeClass('active')
  return false
})
