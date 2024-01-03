#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const Id = '18';
let count = 0;

request.get(url, (error, resp, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(Id)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});