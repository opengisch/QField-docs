$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('div.navbar').addClass('shrink');
  } else {
    $('div.navbar').removeClass('shrink');
  }
});
