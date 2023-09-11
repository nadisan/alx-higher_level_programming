#!/usr/bin/node

if (parseInt(process.argv[2])) {
  let n = 0;
  while (n < parseInt(process.argv[2])) {
    console.log('X'.repeat(parseInt(process.argv[2])));
    n++;
  }
} else {
  console.log('Missing size');
}
