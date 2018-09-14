//alert("hello")

function eq(n1, n2) {
	return (n1.length == n2.length && [...n1].map((v, i) => v - n2[i] == 0).every((v) => v))
}
function lte(n1, n2) {
	return n1 == n2 || n1.length < n2.length || eq(n1, n2)
}

function gt(n1, n2) {
	return !lte(n1, n2)
}

function max(n1, n2) {
	if (lte(n1, n2)) 
		return [n2, n1]
	else 
		return [n1, n2]
}

function add(a, b, c = 0) {
	mx  = max(a, b)
	a = mx[0]
	b = mx[1]
	a = a.split("").map(v => parseInt(v)).reverse()
	b = b.split("").map(v => parseInt(v)).reverse()
	var res = ''
	for (var i = 0; i < a.length; i++) {
		let s = c + a[i] + (b[i]||0)
		c = ~~(s/10)
		res = (s % 10) + res
	}
	if (c) res = c + res
	return res.replace(/^0+/,'') || '0'
}
function trim(a) {
	if (a.indexOf('.') != -1) {
		var p1 = a.replace(/\.\d*/,'').replace(/^0+/,'')
		var p2 = a.replace(/\d*\./,'').replace(/0+$/,'')
		return [p1 + p2, p2.length]
	}
	return [a, 0]
}

function mul(a, b) {
	var neg = 0;
	if (a[0] == '-') {
		neg = 1;
		a = a.slice(1);
	}
	if (b[0] == '-') {
		neg = neg ^ 1;
		b = b.slice(1);
	}
	if (!b || !a) 
		return 0;

	var tz = trim(a)
	a  = tz[0]
	var za = tz[1]
	console.log(za)

	var tz = trim(b)
	b  = tz[0]
	var zb = tz[1]
	console.log(zb)
	
	mx = max(a, b);
	a = mx[0]
	b = mx[1]
	a = a.split("").map(v => parseInt(v)).reverse()
	b = b.split("").map(v => parseInt(v)).reverse()
	console.log(a, b)
	var shift = ''
	var out = '0'
	for (var i = 0; i < b.length; i++) {
		if (b[i]) {
			var c, p;
			var res = '' 
			for (var j = 0, c = 0; j < a.length; j++) {
				p = a[j] * b[i] + c
				c = ~~(p / 10)
				res = (p % 10) + res
			}
			if (c) res = c + res
			res += shift
			out = add(out, res);
			console.log(out)
		}
		shift += '0';
	}
	out = out.replace(/^0+/, '');
	if (!out)
		out = '0';
	else {
		var dz = out.length  - (za + zb)
		if (dz != out.length) {
			console.log('dz', dz)
			if (dz < 0) 
				out = '.' + '0'.repeat(-dz) + out
			else 
				out = out.slice(0,dz) + '.' + out.slice(dz)
		}
		if (neg)
			out = '-' + out
	}
	return out
}
console.log('mult', mul('20', '1234'))
console.log('adding', add("00", "001"))
console.log(mul("1234567990012345", "1234567899542334"))
//console.log("1234")
