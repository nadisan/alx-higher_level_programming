#!/usr/bin/node

let n = parseInt(process.argv[2]);
let m = n;
while (n){
	console.log("X".repeat(m));
	n--;
}
