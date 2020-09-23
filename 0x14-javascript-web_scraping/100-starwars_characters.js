#!/usr/bin/node

const myArgs = process.argv;
let j = 1;
while (j < 9) {
  require('request').get(
    'https://swapi-api.hbtn.io/api/people/?page=' + j.toString(),
    function (err, r, body) {
      if (err) {
        console.log(err);
      } else {
        const json = JSON.parse(body);
        const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[2] + '/';
        for (const film of json.results) {
          for (const i of film.films) {
            if (url === i) {
              console.log(film.name);
            }
          }
        }
      }
    }
  );
  j++;
}
