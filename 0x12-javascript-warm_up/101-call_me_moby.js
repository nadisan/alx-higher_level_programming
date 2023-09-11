#!/usr/bin/node
// prints a message depending of the number of arguments passed

exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    x--;
    theFunction();
  }
};
