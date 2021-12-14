#!/usr/bin/node
// script that computes and prints a factorial
function factorial (a) {
  if (a === 0) {
    return (1);
  }
  if (isNaN(a)) {
    return (1);
  }

  return (factorial(a - 1) * a);
}
const a = parseInt(process.argv[2]);
console.log(factorial(a));
