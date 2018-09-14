//alert("hello")

function max(n1, n2)
{
	if (n1 > n2)
		return n1;
	return n2
}

function min(n1, n2)
{
	if (n1 < n2) return n1;
	return n2;
}

function add(a, b)
{
	var m = max(a.length, b.length)
	if (a.length != m) 
		a = '0'.repeat(m - a.length) + a;
	else
		b = '0'.repeat(m - b.length) + b;

	res = '';
	var c = 0;
	for (i = m-1; i >= 0; i--) {
		a1 = parseInt(a[i]);
		b1 = parseInt(b[i]);
		r = a1 + b1 + c;
		if (r > 9) {
			c = 1;
			r = r - 10;
		}
		else {
			c = 0;
		}
		res += r.toString()
	}
	if (c)
		res += c.toString()
	//console.log(res.split("").reverse().join(""));
	return res.split("").reverse().join("");
}

function mul(a, b)
{
	var neg = 0;
	if (a[0] == '-') {
		neg = 1;
		a = a.slice(1);
		a = a.replace(/^0+/, '');
	}
	if (b[0] == '-') {
		neg = neg ^ 1;
		b = b.slice(1);
		b = b.replace(/^0+/, '');
	}
	if (!b || !a) 
		return 0;
	
	var m1 = min(a, b);
	var m2 = max(a, b);
	var res = '';
	var shift = ''
	var out = '0'
	for (var i = m1.length-1; i >= 0; i--) {
		if (parseInt(m1[i])) {
			res = m2;
			for (var j = 1; j < parseInt(m1[i]); j++)
				res = add(res, m2);
			res += shift;
			out = add(out, res);
		}
		shift += '0';
	}
	out = out.replace(/^0+/, '');
	if (!out)
		out = '0';

	if (neg)
		out = '-' + out;

	return out
}

console.log(add("9999", "9999"))
console.log(mul("1234567990012345", "1234567899542334"))
//console.log("1234")
