#!/usr/bin/node
exports.converter = function (base) {
  return function (y) {
    return parseInt(y, 10).toString(base);
  };
};
