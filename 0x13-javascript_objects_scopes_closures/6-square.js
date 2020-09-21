#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      const array = [];
      for (let j = 0; j < this.width; j++) {
        array.push(c);
      }
      console.log(array.join(''));
    }
  }
};
