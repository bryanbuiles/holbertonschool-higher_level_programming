#!/usr/bin/node

const myArgs = process.argv;
if (myArgs[2] === undefined) {
  console.log('No argument');
} else if (myArgs[3]) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
