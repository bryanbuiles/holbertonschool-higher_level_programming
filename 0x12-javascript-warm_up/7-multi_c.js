#!/usr/bin/node
const myArgs = process.argv;
const integer = parseInt(myArgs[2], 10);
if (isNaN(integer)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < integer; i++) {
    console.log('C is fun');
  }
}
