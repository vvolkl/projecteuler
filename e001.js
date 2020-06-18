var result = 0;
for (var i = 0; i < 1000; ++i) {
  if (!(i % 3) || !(i % 5)) {
    result += i;
  }
}
console.log(result);
