#!/usr/bin/node
const myArgs = process.argv;

require('request').get(myArgs[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    const results = json.results;
    let count = 0;
    for (const items of results) {
      for (const cara of items.characters) {
        if (cara.includes('/18/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
