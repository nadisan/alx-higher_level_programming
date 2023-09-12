#!/usr/bin/node

exports.esrever = function (list) {
  const n = list.length - 1;
  const newlist = [];
  for (let i = 0; i < list.length; i++) {
    newlist[i] = list[n - i];
  }

  return newlist;
};
