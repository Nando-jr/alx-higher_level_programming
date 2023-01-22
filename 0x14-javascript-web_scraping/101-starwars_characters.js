#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function printCharacters (characters, idx) {
  request(characters[idx], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const character = JSON.parse(body).characters;
    printCharacters(character, 0);
  }
});
