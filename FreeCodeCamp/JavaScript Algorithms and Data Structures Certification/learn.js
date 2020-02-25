function telephoneCheck(str) {
  // Good luck!
  var regex = /^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$/g;
  return regex.test(str);
}

let result = telephoneCheck("555-555-5555");
console.log(result);
