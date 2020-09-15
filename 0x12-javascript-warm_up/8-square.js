#!/usr/bin/node
const myArgs = process.argv;
const integer = parseInt(myArgs[2], 10);
let array = [];

if (isNaN(integer)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < integer; i++) {
    array = [];
    for (let j = 0; j < integer; j++) {
      array.push('X');
    }
    console.log(array.join(''));
  }
}
