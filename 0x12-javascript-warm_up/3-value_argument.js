#!/usr/bin/node

const myArgs = process.argv;
if (myArgs[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
