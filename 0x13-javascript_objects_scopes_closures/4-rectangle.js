#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    while (this.height) {
      console.log('X'.repeat(this.width));
      this.height--;
    }
  }
  rotate() {
      const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }
   double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
