#!/usr/bin/node

const myArgs = process.argv;

const fs = require('fs');
fs.readFile(myArgs[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
