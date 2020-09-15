#!/usr/bin/node
const myArgs = process.argv;
const integer = parseInt(myArgs[2], 10);
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
const finalResult = factorial(integer);
console.log(finalResult);
