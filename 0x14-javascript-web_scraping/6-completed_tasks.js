#!/usr/bin/node

const myArgs = process.argv;

require('request').get(myArgs[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    const dicti = {};
    let count = 1;
    const json = JSON.parse(body);

    for (let key = 0; key < json.length; key++) {
      if (json[key].completed === true) {
        if (!(json[key].userId in dicti)) {
          count = 1;
        }
        dicti[json[key].userId] = count++;
      }
    }
    console.log(dicti);
  }
});
