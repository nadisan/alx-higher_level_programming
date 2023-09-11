#!/usr/bin/node
// prints a message depending of the number of arguments passed

function fact (a) {
  if (a === 1 || isNaN(a)) {
	 return (1);
  } else if (a > 1) {
    return (a * fact(a - 1));
  }
}

console.log(fact(parseInt(process.argv[2])));
