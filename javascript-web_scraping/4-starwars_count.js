#!/usr/bin/node
/*
 * Script that prints the number of movies where
 *  the character Wedge Antilles is present.
 */
const args = process.argv;
const req = require('request');

if (args.length === 3) {
  req.get(args[2], function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      const character = JSON.parse(body);
      let count = 0;
      for (const movie of character.results) {
        for (const person of movie.characters) {
          if (person.endsWith('/18/')) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
