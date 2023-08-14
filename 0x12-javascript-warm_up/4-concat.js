#!/usr/bin/node

if (process.argv.length >= 3) {
  const args_res = process.argv[2].concat(' is ', process.argv[3]);
  console.log(args_res);
} else {
  const args_res = 'undefined'.concat(' is ', process.argv[3]);
  console.log(args_res);
}
