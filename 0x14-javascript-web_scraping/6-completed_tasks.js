#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, _response, body) {
  if (error) {
    console.log(error)
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i){
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completedTasksByUsers[userId]){
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }
    console.log(completedTasksByUsers);
  }
});
