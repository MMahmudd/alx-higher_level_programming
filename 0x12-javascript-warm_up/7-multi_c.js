#!/usr/bin/node

let ii = 0;
const nums = parseInt(process.argv[2]);

if (process.argv.length < 3 || isNaN(nums)) {
  console.log('Missing number of occurrences');
} else {
  while (ii < process.argv[2]) {
    console.log('C is fun');
    ii++;
  }
}
