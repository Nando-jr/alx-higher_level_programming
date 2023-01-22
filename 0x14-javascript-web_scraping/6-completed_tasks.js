#!/usr/bin/node
// A script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const tasknum = {};
    for (const task of tasks) {
      if (task.completed) {
        if (!tasknum[task.userId]) {
          tasknum[task.userId] = 0;
        }
        ++tasknum[task.userId];
      }
    }
    console.log(tasknum);
  }
});
