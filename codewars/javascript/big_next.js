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
