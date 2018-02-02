$('.home-map__toggle').click(function () {
  //$(this).hasClass('active') ? $(this).parent().find('img').attr('src', './static/img/assets/home-map/map.jpg') : $(this).parent().find('img').attr('src', './static/img/assets/home-map/map-active.jpg')
  $(this).toggleClass('active')
  $('.home-map').toggleClass('active')
  $('.home-map__item-list').removeClass('active')
  return false
})

$('.home-map__item').click(function () {
  $('.home-map__item-list').removeClass('active')
  $('.home-map__item').removeClass('active')
  if($(this).hasClass('active')) {
    $(this).removeClass('active')
    $(this).next().removeClass('active')
  }
  else {
    $(this).addClass('active')
    $(this).next().toggleClass('active')
  }

  return false
})

$(document).mouseup(function (e){ // событие клика по веб-документу
  var div = $('.home-map__item-list'); // тут указываем ID элемента
  if (!div.is(e.target) // если клик был не по нашему блоку
      && div.has(e.target).length === 0) { // и не по его дочерним элементам
    div.removeClass('active'); // скрываем его
  }
});

$('.home-map .close-button').click(function () {
  $('.home-map__item-list').removeClass('active')
  $('.home-map__item').removeClass('active')
  return false
})
