#!/usr/bin/node
// prints a message depending of the number of arguments passed

function add (a, b) {
  return (a + b);
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
