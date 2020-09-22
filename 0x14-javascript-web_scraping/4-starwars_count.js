#!/usr/bin/node
const myArgs = process.argv;
if (
  myArgs[2] === 'https://swapi-api.hbtn.io/api/films' ||
  myArgs[2] === 'https://swapi-api.hbtn.io/api/films/'
) {
  const request = require('request');
  const options = {
    url: 'https://swapi-api.hbtn.io/api/people/18/',
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'Accept-Charset': 'utf-8'
    }
  };
  request(options, function (err, res, body) {
    if (err) {
      console.error(err);
      return;
    }
    const json = JSON.parse(body);
    console.log(json.films.length);
  });
}
