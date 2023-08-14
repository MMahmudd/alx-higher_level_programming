#!/usr/bin/node

const sizze = process.argv.length;

if (sizze <= 3) {
  console.log(0);
} else {
  const new_A = process.argv.map(Number);
  new_A.slice(2, sizze);
  new_A.sort((a, b) => a - b);
  console.log(new_A[new_A.length - 2]);
}
