#!/usr/bin/node

const data = require('./101-data').dict;
const newdict = {};
for (const key in data) {
  if (newdict[data[key]] === undefined) {
    newdict[data[key]] = [key];
  } else {
    newdict[data[key]].push(key);
  }
}
console.log(newdict);
