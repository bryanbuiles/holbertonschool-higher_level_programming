#!/usr/bin/node

const myArgs = process.argv;
const integer = parseInt(myArgs[2], 10);
if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + integer);
}
