#!/usr/bin/node

const myArgs = process.argv;

const fs = require('fs');
fs.readFile(myArgs[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString().trim());
  }
});
