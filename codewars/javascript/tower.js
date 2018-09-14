function lastDigit(as)
{
  
	var l = as.length
	if (l == 0) return 1;
  for (var c = l-2; c >= 0; c--) {
      if (as[c] == 0) 
        as[c] = Math.pow(as[c], as[c+1])
      else if (as[c+1] == 0)
        as[c] = 1
  }

	if (as.length == 1) return as[0] % 10
  if (as.length == 2)
        as.push(1) 
    // chineese remainder theorem 10 = 2 * 5
    // solve power % 2 and power % 5 and solve the equation
    // 
	  var a, b, c;
	  var r1, r2;
    a = as[0]
    b = as[1]
    c = as[2]
    r1 = a % 2
    if (a % 5 != 0) {
        r2 = b % 4
        
        if (r2 == 2 && c >= 2) 
            r2 = 0
        else if (r2 == 3) 
            r2 = Math.pow(3,(c % 2))

		    r2 = Math.pow(a%5,r2) % 5
	  }
	  else {
	        r2 = 0	
	  }


    // find n such that it returns r1 when n % 2 and r2 when n % 5
    // 2 * x + r1 = n
    // 5 * y + r2 = n
	
	for(var i = 0; i < 5; i++) {
        if ((2 * i + r1 - r2) % 5 == 0)
            return 2 * i + r1
	}
}

function lastDigit2(as){
  return as.reduceRight(function(pow, base, index, array) {
    return pow === 0 ? 1 : ( +pow == 1 ? base : Math.pow(base % 100, +pow % 4 + 4));
  }, 1) % 10;
}
console.log(lastDigit2([452954,834239]));
console.log(lastDigit([452954,834239]) == 4);
/***
console.log(power_tower([]         ) ==  1);
console.log(power_tower([0,0]      ) ==  1); // 0 ^ 0
console.log(power_tower([0,0,0]    ) ==  0); // 0^(0 ^ 0) = 0^1 = 0
console.log(power_tower([1,2]      ) ==  1);
console.log(power_tower([3,4,5]    ) ==  1);
console.log(power_tower([4,3,6]    ) ==  4);
console.log(power_tower([7,6,21]   ) ==  1);
console.log(power_tower([12,30,21] ) ==  6);
console.log(power_tower([2,2,2,0]  ) ==  4);
console.log(power_tower([937640,767456,981242] ) ==  0);
console.log(power_tower([123232,694022,140249] ) ==  6);
console.log(power_tower([499942,898102,846073] ) ==  6);

var r1 = Math.floor(Math.random() * 100);
var r2 = Math.floor(Math.random() * 10);

console.log(power_tower([]) ==  1);
console.log(power_tower([r1]) ,  r1 % 10);
console.log(power_tower([r1, r2]) ==  Math.pow(r1 % 10, r2) % 10);
***/
