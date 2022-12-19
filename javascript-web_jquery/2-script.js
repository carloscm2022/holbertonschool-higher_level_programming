#!/usr/bin/node
/*
 * Script that updates the text color of the HTML tag HEADER to red (#FF0000)
 * when the user clicks on the tag DIV#red_header.
 */
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
