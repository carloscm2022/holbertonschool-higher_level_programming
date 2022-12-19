#!/usr/bin/node
/*
 * Script that toggles the class of the HTML tag HEADER to red (#FF0000)
 * when the user clicks on the tag DIV#toggle_header.
 */
$(document).ready(function () {
  $('#toggle_header').click(function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').toggleClass('red');
    } else {
      $('header').removeClass('red');
      $('header').toggleClass('green');
    }
  });
});
