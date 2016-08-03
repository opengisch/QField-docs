$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('div.navbar').addClass('shrink');
    $('.navbar-brand>span>img').addClass('unobtrusive');
    $('.shadow-background>img').addClass('unobtrusive');
  } else {
    $('div.navbar').removeClass('shrink');
    $('.navbar-brand>span>img').removeClass('unobtrusive');
    $('.shadow-background>img').removeClass('unobtrusive');
  }
});
