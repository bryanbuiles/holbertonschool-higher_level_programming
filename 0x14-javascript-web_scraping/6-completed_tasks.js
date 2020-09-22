#!/usr/bin/node

const myArgs = process.argv;

require('request').get(myArgs[2] + '?completed=true', function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    const dicti = {};
    let count = 1;
    const json = JSON.parse(body);
    for (let key = 0; key < json.length; key++) {
      if (key !== 0) {
        if (json[key - 1].userId !== json[key].userId) {
          count = 1;
        } else {
          count++;
        }
        dicti[json[key].userId] = count;
      }
    }
    console.log(dicti);
  }
});
