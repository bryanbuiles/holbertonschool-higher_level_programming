#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h)) {
    } else if (w <= 0 || h <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const array = [];
      for (let j = 0; j < this.width; j++) {
        array.push('X');
      }
      console.log(array.join(''));
    }
  }
}
module.exports = Rectangle;
