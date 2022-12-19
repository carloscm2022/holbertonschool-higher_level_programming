#!/usr/bin/node
/*
 * Script fetches and replaces the name of this URL:
 * https://swapi-api.hbtn.io/api/people/5/?format=json
 * The name must be displayed in the HTML tag DIV#character
 */
$(document).ready(function () {
  const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(URL, function (data, status) {
    if (status === 'success') {
      $('#character').text(data.name);
    }
  });
});
