#!/usr/bin/node
/*
 * Script that writes a string to a file.
 */
const args = process.argv;
const fs = require('fs');

if (args.length === 4) {
  fs.writeFile(args[2], args[3], 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
}
