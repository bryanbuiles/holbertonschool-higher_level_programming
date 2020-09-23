#!/usr/bin/node
const myArgs = process.argv;

require('request').get(myArgs[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    const json = body.toString();
    const fs = require('fs');
    fs.writeFile(myArgs[3], json, 'utf8', (err) => {
      if (err) throw err;
    });
  }
});
