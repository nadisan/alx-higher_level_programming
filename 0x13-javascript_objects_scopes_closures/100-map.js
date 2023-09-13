#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
const mappedlist = list.map(function (e, index) {
  return (e * index);
});
console.log(mappedlist);
