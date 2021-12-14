#!/usr/bin/node
// script that prints the addition of 2 integers
function add (a, b) {
  console.log(a + b);
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
add(a, b);
