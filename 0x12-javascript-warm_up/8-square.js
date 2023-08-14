#!/usr/bin/node

const sizze = process.argv[2];
let charcs = '';
if (process.argv.length < 3 || isNaN(sizze)) {
  console.log('Missing size');
} else {
  for (let ii = 0; ii < size; ii++) {
    charcs = '';
    for (let jj = 0; jj < sizze; jj++) charcs += 'X';
    console.log(charcs);
  }
}
