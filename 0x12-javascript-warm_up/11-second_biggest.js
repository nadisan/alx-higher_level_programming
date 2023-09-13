#!/usr/bin/node
// prints a message depending of the number of arguments passed

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const secondLargest = process.argv.sort((a, b) => b - a);
  console.log(secondLargest[3]);
}
