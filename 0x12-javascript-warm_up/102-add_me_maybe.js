#!/usr/bin/node
// prints a message depending of the number of arguments passed

exports.addMeMaybe = function (number, theFunction){
	number += 1;
	theFunction(number);
}
