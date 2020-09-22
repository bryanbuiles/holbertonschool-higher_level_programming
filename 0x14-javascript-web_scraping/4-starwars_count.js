#!/usr/bin/node
const myArgs = process.argv;

const request = require('request');
const options = {
  url: myArgs[2],
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
  const results = json.results;
  let count = 0;
  for (const items of results) {
    for (const cara of items.characters) {
      if (cara === 'https://swapi-api.hbtn.io/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
