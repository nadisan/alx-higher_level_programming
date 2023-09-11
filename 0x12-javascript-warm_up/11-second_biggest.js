#!/usr/bin/node
// prints a message depending of the number of arguments passed

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.sort();
  console.log(arr.reverse()[1]);
}
