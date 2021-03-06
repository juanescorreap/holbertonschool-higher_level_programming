#!/usr/bin/node

const previousSquare = require('./5-square');

// Class Square that defines a square and inherits from Square

class Square extends previousSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
}

module.exports = Square;
