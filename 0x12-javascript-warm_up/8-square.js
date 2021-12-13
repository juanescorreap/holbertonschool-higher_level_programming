#!/usr/bin/node
// Write a script that prints a square
const size = parseInt(process.argv[2]);
const myArray = [];
if (size) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      myArray[j] = 'X';
    }
    console.log(myArray.join(''));
  }
} else {
  console.log('Missing size');
}
