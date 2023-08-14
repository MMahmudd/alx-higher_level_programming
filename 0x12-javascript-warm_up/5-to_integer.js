#!/usr/bin/node

const nums = parseInt(process.argv[2]);

if (process.argv.length < 3 || isNaN(nums)) {
  console.log('Not a number');
} else {
  console.log('My number: '.concat(nums));
}
