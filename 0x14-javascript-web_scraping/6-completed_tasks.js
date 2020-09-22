#!/usr/bin/node

const myArgs = process.argv;

require('request').get(myArgs[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    const dicti = {};
    let count = 1;
    const lista = [];
    const json = JSON.parse(body);
    for (const items of json) {
      if (items.completed === true) {
        lista.push(items);
      }
    }
    for (let key = 0; key < lista.length; key++) {
      if (key !== 0) {
        if (lista[key - 1].userId !== lista[key].userId) {
          count = 1;
        } else {
          count++;
        }
        dicti[lista[key].userId] = count;
      }
    }
    console.log(dicti);
  }
});
