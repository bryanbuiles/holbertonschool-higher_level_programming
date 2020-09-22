#!/usr/bin/node
const myArgs = process.argv;

const request = require('request');
const options = {
  url: myArgs[2],
  method: 'GET'
};
request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    const results = json.results;
    let count = 0;
    for (const items of results) {
      for (const cara of items.characters) {
        if (cara === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
