#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const film = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${film}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    for (const character of data) {
      request(character, (error, response, value) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(value).name);
      });
    }
  }
});
