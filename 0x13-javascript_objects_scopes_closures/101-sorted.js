#!/usr/bin/node
const dict = require('./101-data').dict;
const dicti = {};
let lista2 = [];
for (const key in dict) {
  lista2 = [];
  for (const values in dict) {
    if (dict[key] === dict[values]) {
      lista2.push(values);
    }
  }
  dicti[dict[key]] = lista2;
}
console.log(dicti);
