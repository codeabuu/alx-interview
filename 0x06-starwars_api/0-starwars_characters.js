#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Assuming the movie ID is passed as the first positional argument

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    console.log(`Characters in ${film.title}:`);
    film.characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error('Error:', error);
        }
      });
    });
  }
});
