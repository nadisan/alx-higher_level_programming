#!/usr/bin/node
// prints a message depending of the number of arguments passed

const myVar = parseInt(process.argv[2]);
if (myVar) {
  console.log('My number: ' + myVar);
} else {
  console.log('Not a number');
}
