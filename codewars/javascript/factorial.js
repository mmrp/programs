function factorial(n) {
  var res = [1];
  for (var i = 2; i <= n; ++i) {
    var c = 0;
    for (var j = 0; j < res.length || c !== 0; ++j) {
      c += (res[j] || 0) * i;
      res[j] = c % 10;
      c = Math.floor(c / 10);
    }
  }
  return res.reverse().join("");
}
