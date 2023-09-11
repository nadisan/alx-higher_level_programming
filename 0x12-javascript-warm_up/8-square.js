#!/usr/bin/node

let n = parseInt(process.argv[2]);
const m = n;
while (n > 0) {
  console.log('X'.repeat(m));
  n--;
}
