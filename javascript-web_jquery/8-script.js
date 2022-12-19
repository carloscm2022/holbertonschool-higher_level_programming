#!/usr/bin/node
/*
 * Script fetches fetches and lists all movies title by using this URL:
 * https://swapi-api.hbtn.io/api/films/?format=json
 * All movie titles must be list in the HTML tag UL#list_movies
 */
$(document).ready(function () {
  const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(URL, function (data, status) {
    if (status === 'success') {
      for (let i = 0; i < data.results.length; i++) {
        $('#list_movies').append('<li>' + data.results[i].title + '</li>');
        // console.log(data.results[i].title);
        // $('#character').text(data.name);
      }
    }
  });
});
