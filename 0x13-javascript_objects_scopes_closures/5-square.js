#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // call the super class constructor and pass in the name parameter
  }
}
module.exports = Square;
