#!/usr/bin/node
let contador = 0;
exports.logMe = function (item) {
  contador = contador + 1;
  console.log(contador + ': ' + item);
};
