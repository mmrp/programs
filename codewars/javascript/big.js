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
	return res
}

	
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

//assumption a, b are positive
const lessthan = (a, b) => a.length < b.length || ((a.length == b.length) && a < b)

function bigAdd(a, b) {
	let aneg, bneg
	[aneg, a, bneg, b] = convert(a, b)

	if (a == b) return "0"
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
	b = b.toString()
	if (b[0] == '-') 
		b = b.slice(1)
	else
		b = '-' + b

	return bigAdd(a, b)
}
console.log(bigAdd("123123", 2234))
console.log(bigAdd("123123", -2234))
console.log(bigSub("123123", 2234))
