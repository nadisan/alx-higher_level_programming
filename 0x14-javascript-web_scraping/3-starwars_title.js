#!/usr/bin/node

const request = require('request');
let starwars = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
request(starwars, function(_error, _response, body){
 body = JSON.parse(body); 
 console.log(body.title);
 }
 )
