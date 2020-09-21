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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        const array = [];
        for (let j = 0; j < this.width; j++) {
          array.push(c);
        }
        console.log(array.join(''));
      }
    }
  }
}
module.exports = Rectangle;
module.exports = Square;
