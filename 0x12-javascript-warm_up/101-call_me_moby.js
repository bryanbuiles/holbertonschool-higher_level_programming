#!/usr/bin/node
exports.callMeMoby = function (a, anotherF) {
  for (let i = 0; i < a; i++) {
    anotherF();
  }
};
