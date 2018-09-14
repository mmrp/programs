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

//assumption a, b are positive
const lessthan = (a, b) => a.length < b.length || ((a.length == b.length) && a < b)
const gte = (a, b) => !lessthan(a,b)

function convert(a, b) {
	let aneg = false
	let bneg = false
	a = a.toString()
	b = b.toString()

	if (a[0] == '-') {
		aneg = true
		a = a.slice(1)
	}

	if (b[0] == '-') {
		bneg = true
		b = b.slice(1)
	}
	return [aneg, a, bneg, b]
}


//code I liked from somebody else solution
function long_add(a, b)
{
	a = a.split(""); b = b.split("") 
	let c, v, res; 
	res = '', c = 0
	while (a.length || b.length || c) {
		v = c + ~~a.pop() + ~~b.pop()  
		c = v >= 10 ? 1: 0;
		res = v % 10 + res
	}
	return res
}

//code I liked from somebody else solution
function long_sub(a, b)
{
	a = a.split(""); b = b.split("")
	let c, v, res;
	res = '', c = 0
	while (a.length || b.length || c) {
		c += ~~a.pop() - ~~b.pop()
		res = (c+10) % 10 + res
		c = -(c<0)
	}
	return res.replace(/^0+/,'') || '0'
}

function long_mul(a, b) 
{
	if (lessthan(a, b))
		[a, b] = [b, a]

	a = a.split("").reverse(); b = b.split("").reverse()
	let c, v, res;
	let i, j
	res = []
	for (i = 0; i < b.length; i++) {
		for (j = 0, c = 0; j < a.length; j++) {
			v = c + (res[i+j] || 0) + a[j] * b[i]
			res[i+j] = v % 10
			c = Math.floor(v/10)
		}
		res[i+j] = c 
	}
	return res.map((d)=>d.toString()).reverse().join("").replace(/^0+/,'') || '0' 
}

function long_div(a, b)
{
	if (lessthan(a, b))
		return ["0", a]
	
	let d, quo, rem, loops;

	loops = a.length - b.length + 1
	quo = ''
	rem = a.slice(0, b.length)	
	a = a.slice(b.length)
	for (let i = 0; i < loops; i++) {
		for (d = 0; gte(rem, b); d++) {
			rem = long_sub(rem, b)
		}
		quo = (quo == '0'? '': quo) + d.toString()
		rem = ((rem == '0')? '' : rem) + (a[0] || '')
		a = a.slice(1)
	}
	return [quo, rem.replace(/^0+/,'')]
}

function bigAdd(a, b) {
	let aneg, bneg
	[aneg, a, bneg, b] = convert(a, b)

	let rneg = false
	if (aneg == bneg) {
		res = long_add(a, b)
		rneg = aneg
	}
	else { 
		rneg = aneg
		if (lessthan(a, b)) {
			[a, b] = [b, a]
			rneg = bneg
		}
		res = long_sub(a, b)	
	}
	res = rneg ? '-' + res: res
	return res
}

function bigSub(a, b) {
	if (a == b) return "0"

	b = b.toString()
	if (b[0] == '-') 
		b = b.slice(1)
	else
		b = '-' + b

	return bigAdd(a, b)
}

function bigMul(a, b) {
	let aneg, bneg
	[aneg, a, bneg, b] = convert(a, b)
	
	let rneg
	if (aneg == bneg)
		rneg = aneg
	else
		rneg = '-'

	let res
	res = long_mul(a, b)
	res = rneg ? '-' + res: res
	return res
}

function bigDiv(a, b) {
	let aneg, bneg
	[aneg, a, bneg, b] = convert(a, b)

	let rneg
	if (aneg == bneg)
		rneg = aneg
	else
		rneg = '-'

	let res = long_div(a, b)
	res = res[0]
	res = rneg ? '-' + res: res
	return res
}
/*
console.log(bigAdd("1", 1))
if (false) {
console.log(bigAdd("123123", -2234))
console.log(bigSub("123123", 2234))
console.log(bigMul("438", -470))
console.log(bigSub(114, 69))
console.log(bigDiv('666', 69))
for (let i = 0; i < 1000; i++) {
	a = Math.floor(Math.random() * 10000000000000000)
	b = Math.floor(Math.random() * 10000000000000000)
	if (bigDiv(a, b) != Math.floor(a/b)) {
		console.log('fail', a, b)
		break
	}
}
console.log(bigDiv('123333333333333333333333354356798965342567894323434353543431646843513684456463413','123124234557687343415233441687654346846543435'))
}
*/


function generate_primes(maxn) 
{
	var primes = [2]
	let max_number = Math.ceil(Math.sqrt(maxn))
	let n = primes[primes.length - 1] + 1
	for (n = 3; n <= max_number; n += 2) {
		let last = Math.ceil(Math.sqrt(n))
		let is_prime = true
		for (let i = 0; primes[i] <= last; i++) {
			if (n % primes[i] == 0) {
				is_prime = false
				break
			}
		}
		if (is_prime)
			primes.push(n)
	}
	return primes
}
// our sieve function which will return a list of primes
// up to the limit argument passed
var primes = [];
var primes_rmap = [];
function sieve(limit) {
	if (primes.length)
		return
	var bools = [];

	// generate a list of booleans all set to true initially
	// the array is indexed from 2 to limit representing all numbers
	// e.g. [true, true, true, true] = [2, 3, 4, 5]
	for (var i = 1; i < limit; i++) { bools.push(true); } 

	// loop from 2 to limit setting the composite numbers to false
	// we start from 2 because we know 1 is not a prime number
	for (var i = 2; i < limit; i++) {
		if (bools[i-2]) {
			for (var j = i*2; j <= limit; j += i) {
				bools[j-2] = false;    
			}
		}
	}

	// now generate the list of primes only where
	// there is a true value in the bools array
	for (var p = 0; p < bools.length; p++) {
		if (bools[p]) { primes.push(p+2); }
	}

	for (i = 0; i < primes.length; i++)
  		primes_rmap[primes[i]] = i+1 

	//return primes;
} 

function factors(number) {
	sieve(10000000);//Number.MAX_SAFE_NUMBER)

	let f = []
	let last = Math.ceil(Math.sqrt(number))

	for (i = 0; primes[i] <= last && number > 1; i++) {
		while (number % primes[i] == 0) {
			number = number / primes[i]
			f.push(primes[i])
		}
	}
	if (number > 1)
		f.push(number)

	return f.sort((a,b)=>a-b)
}

function encode(number) {
	if (number == 2) {
		return "[[]]"
	}

	let s = [] 
	let f = factors(number)
	for (let i = 0; i < f.length; i++) 
		s.push(encode(primes_rmap[f[i]]))
	r = "[" + s.join(", ") + "]"
	return r
}

function dec2bin(n) {
	let s = ''
	while (n) {
		s = n%2 + s
		n = Math.floor(n/2)
		console.log(s, n)
	}
	return s
}
function bin2dec(s) {
	console.log('bin2dec', s)
	return [...s].reverse().reduce((r,v,i)=> parseInt(r) + ((v == '1')? Math.pow(2,i): 0))
}

function prb_decode(number) {
	b = dec2bin(number) + '1'
	lcount = [...b].filter((a) => a == '1').length 
	rcount = [...b].filter((a) => a == '0').length
	b = b + '0'.repeat(lcount - rcount)
	return b
}

//console.log(generate_primes(Number.MAX_SAFE_INTEGER))
/**/
function prb_encode(num) {
	console.log('----------------')
	s = encode(num)
	if (num == 2)
		return s
	console.log(num, s)
	s = s.slice(1,-1).replace(/[ ,]/g, '').replace(/\[/g, '1').replace(/\]/g, '0').replace(/0+$/g, '')
	console.log(s)
	s = bin2dec(s.slice(0,-1))
	console.log(s)
}
//for (let i = 2; i < 100; i++) {
//	console.log(10006, prb_encode(10006))
//}
//console.log(generate_primes(Number.MAX_SAFE_INTEGER))
console.log(prb_encode(46))
console.log(prb_decode(185))
