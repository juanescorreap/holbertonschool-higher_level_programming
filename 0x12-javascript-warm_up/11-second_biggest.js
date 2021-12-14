#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
if (process.argv.length === 2) {
  console.log('0');
}
if (process.argv.length === 3) {
  console.log('1');
}
if (process.argv.length > 3) {
  const myArray = [];
  let i = 2;
  while (process.argv[i]) {
    myArray[i - 2] = parseInt(process.argv[i]);
    i = i + 1;
  }
  const max = Math.max.apply(null, myArray);
  myArray.splice(myArray.indexOf(max), 1);
  console.log(Math.max.apply(null, myArray));
}
