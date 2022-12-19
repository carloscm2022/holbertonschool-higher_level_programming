#!/usr/bin/node
/*
 * Script that computes the number of tasks completed by user id.
 */
const args = process.argv;
const req = require('request');

if (args.length === 3) {
  req.get(args[2], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const myResp = JSON.parse(body);
      const myDict = {};
      for (let i = 0; i < myResp.length; i++) {
        if (myResp[i].completed === true) {
          if (myDict[myResp[i].userId] === undefined) {
            myDict[myResp[i].userId] = 1;
          } else {
            myDict[myResp[i].userId] += 1;
          }
        }
      }
      console.log(myDict);
    }
  });
}
