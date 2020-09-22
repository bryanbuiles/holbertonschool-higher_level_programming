#!/usr/bin/node

const myArgs = process.argv;
const content = myArgs[3];
const fs = require('fs');
fs.writeFile(myArgs[2], content, 'utf8', (err) => {
  if (err) throw err;
});
