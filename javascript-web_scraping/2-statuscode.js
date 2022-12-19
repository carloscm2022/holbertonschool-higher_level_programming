#!/usr/bin/node
/*
 * Script that display the status code of a GET request.
 */
const args = process.argv;
const req = require('request');

if (args.length === 3) {
  req.get(args[2], function (error, response) {
    if (error) {
      console.log(error);
    } else {
      console.log('code: ' + response.statusCode);
    }
  });
}
