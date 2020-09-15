#!/usr/bin/node
const myArgs2 = process.argv;
const myArgs = process.argv.slice(2);
if (myArgs2[2] === undefined) {
  console.log(0);
} else if (myArgs2[3] === undefined) {
  console.log(0);
} else {
  const lista = [];
  for (let i = 0; i < myArgs.length; i++) {
    const integer = parseInt(myArgs[i], 10);
    lista.push(integer);
  }
  const maxValue = Math.max(...lista);
  let integer = 0;
  for (let j = 0; j < lista.length; j++) {
    if (lista[j] > integer && lista[j] !== maxValue) {
      integer = lista[j];
    }
  }
  console.log(integer);
}
