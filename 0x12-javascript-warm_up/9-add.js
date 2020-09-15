#!/usr/bin/node
const myArgs = process.argv;
const integer = parseInt(myArgs[2], 10);
const integer2 = parseInt(myArgs[3], 10);

function add (a, b) {
  const result = a + b;
  return result;
}
const finalResult = add(integer, integer2);
console.log(finalResult);
