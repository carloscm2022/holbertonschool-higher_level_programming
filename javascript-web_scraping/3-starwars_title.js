#!/usr/bin/node
/*
 * Script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 */
const args = process.argv;
const req = require('request');

if (args.length === 3) {
  const URL = 'https://swapi-api.hbtn.io/api/films/' + args[2];
  req.get(URL, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      const movie = JSON.parse(body);
      console.log(movie.title);
    }
  });
}
