#!/usr/bin/node
/*
 * Script that gets the contents of a webpage and stores it in a file.
 */
const args = process.argv;
const fs = require('fs');
const req = require('request');

if (args.length === 4) {
  const URL = args[2];
  const fpath = args[3];
  req.get(URL, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      // console.log(body);
      fs.writeFile(fpath, body, 'utf-8', (error) => {
        if (error) {
          console.log(error);
        }
      });
    }
  });
}
