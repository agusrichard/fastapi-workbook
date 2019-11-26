function destroyer(arr, ...args) {

      return arr.filter(item => args.indexOf(item) < 0);
}

let result = destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3);
console.log(result);
