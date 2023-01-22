#!/usr/bin/node
// A script that prints the number of movies where the
// character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let n = 0;
    for (const d of data) {
      for (const c of d.characters) {
        if (c.includes('18')) {
          ++n;
        }
      }
    }
    console.log(n);
  }
});
