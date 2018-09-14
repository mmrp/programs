function long_add(a, b)
{
	var m, n;
	m = a
	n = b
	if (greater(b, a)) {
		m = b
		n = a
	}
	m = m.replace(/^0+/, '')
	n = n.replace(/^0+/, '')
	n = '0'.repeat(m.length - n.length) + n
	m = m.split("").reverse().map((w)=>parseInt(w))
	n = n.split("").reverse().map((w)=>parseInt(w)) 
	r = ''
	var c = 0
	//console.log(a, b)
	for (var i = 0; i < m.length; i++) {
		var d = c + m[i] + n[i]
		c = Math.floor(d / 10)
		d = d % 10
		//console.log(d, c)
		r += d.toString()
	}
	r += c.toString()
	return r.split("").reverse().join("").replace(/^0+/, '')
}
function long_mul(a, b)
{
	var m = a
	var n = b
	if (greater(b, a)) {
		m = b
		n = a
	}
	m = m.replace(/^0+/, '').split("").reverse().map((w)=>parseInt(w))
	n = n.replace(/^0+/, '').split("").reverse().map((w)=>parseInt(w)) 

	//console.log(m, n)
	var r = '0'
	for (var i = 0; i < n.length; i++) {
		var c = 0
		var s = 0
		var d = n[i]
		var tr = ''
		m * d
		for (var j = 0; j < m.length; j++) {
			s = d * m[j] + c
			c = Math.floor(s / 10)
			s = s % 10
			tr += s.toString()
			//console.log(tr)
		}
		tr += c.toString()
		r = long_add(r, tr.split("").reverse("").join("") + '0'.repeat(i))
		//console.log('in mul', tr, r)
	}
//	r = r.split("").reverse().join("").replace(/^0+/, '')
	if (!r) 
		return '0'
	return r
	

}

function long_mul_add(a, b)
{
	var m = a
	var n = b
	if (greater(b, a)) {
		m = b
		n = a
	}
	m = m.replace(/^0+/, '')
	n = n.replace(/^0+/, '')
	var r = '0'
	//console.log(n.length)
	for (var i = '0'; lesser(i, n); i = long_add(i, '1')) {
		r = long_add(r, m)
		//console.log('in mul', r, m)
	}
	return r

}


function long_sub(a, b)
{
	var m, n;
	var neg = false
	m = a
	n = b
	if (greater(b, a)) {
		m = b
		n = a
		neg = true
	}
	m = m.replace(/^0+/,'')
	n = n.replace(/^0+/,'')
	n = '0'.repeat(m.length - n.length) + n
	m = m.split("").reverse().map((w)=>parseInt(w))
	n = n.split("").reverse().map((w)=>parseInt(w)) 
	r = ''
	s = 0
	//console.log(m, n)
	for (var i = 0; i < n.length; i++) {
		if (s) {
			if (m[i])
				s = 0
			m[i] -= 1
		}
		v = s * 10 + m[i] - n[i]			
		if (v < 0) {
			v += 10
			s = 1
		}
		//console.log(v)
		r += v.toString()
	}

	r = r.split("").reverse().join("").replace(/^0+/, '') 
	if (neg) 
		r = '-' + r
	if (!r)
		r = '0'
	return r
}

function greater_or_equal(a, b)
{
	a = a.replace(/^0+/, '')
	b = b.replace(/^0+/, '')
	return a == b || greater(a, b);
}

function greater(a, b)
{
	a = a.replace(/^0+/, '')
	b = b.replace(/^0+/, '')
	
	var d = a.length - b.length
	if (d == 0)
		return a > b
	else
		return d > 0
}

function lesser(a, b)
{
	return !greater_or_equal(a, b)
}

function long_div(b, a)
{
	//console.log('long div', b, a)
	b = b.split("")
	var acc = '0';
	var i = 0;
	while (greater(a, acc) && i < b.length) {
		acc += b[i];
		i++;
	}

	var c = 0;
	var q = ''
	while (greater_or_equal(acc, a)) {
		acc = long_sub(acc, a);
		c += 1;
	}
	q += c.toString()
	var loops = 0
	while (i < b.length) {
		var j = i
		while (greater(a, acc) && i < b.length) {
			acc += b[i];
			i++;
		}
		//console.log(a, acc, i, j)
		if (i > j)
			q += '0'.repeat(i-j-1)
		
		if (greater(a, acc)) {
			return q + '0';
		}

	
		c = 0;
		while (greater_or_equal(acc, a)) {
			acc = long_sub(acc, a);
			c += 1;
			//console.log('count: ', c)
		}
		q += c.toString()
		if (loops++ > 400) {
			console.log('breaking', acc, 'q:', q)
			break
		}
	}
	return q;
}


function bin(s)
{
	var r = ''
	var loops = 0
	//console.log(s)
	while (greater_or_equal(s, "2")) {
		if (parseInt(s[s.length-1]) % 2)
			r += '1'
		else
			r += '0'
		s = long_div(s, "2")
		//console.log(s, r)
		if (loops++ >  400) {
			console.log('done', loops)
			break
		}
	}
	r += s
	return r.split("").reverse().join("")
}

function isqrt(n) 
{
	if (lesser(n, "2"))
		return n;
	s = isqrt(long_div(n, "4")) 
	s = long_add(s, s)
	l = long_add(s, "1")
	if (greater(long_mul(l, l), n))
		return s
	else
		return l
}

function sqrt(n) 
{
	var x1 = 1
	var x2 = n 
	var x3;
	var loops = 0
	console.log('in sqrt')
	while (1) {
		x3 = Math.floor((x1+x2)/2)
		console.log(x1, x2, x3)
		if (x3 * x3 <= n) {
			if ((x3+1) * (x3+1) > n)
				break
			x1 = x3
		}
		else {
			x2 = x3
		}
		if (loops++ > 400)
			break
	}
	return [...x3.toString()]
}
//sqrt(1231231231221312)
console.log(sqrt("1231111111111111111111111123423453456456756767823423423421312234324545645732434654656765"))
console.log(isqrt("1231111111111111111111111123423453456456756767823423423421312234324545645732434654656765"))

//bin("15");
//console.log('long div r', long_div("21", "2"))
//console.log(greater_or_equal("2", "02"))
//console.log('long div', long_div("0", "341212"))
//console.log('long div', long_div("12341234567", "341212"))
//console.log('long div', long_div("1111111122222222222224567899999999999999676786786786786767","1234234234234123123454457676878989098"))
//console.log(greater("12343455", "9"))
//console.log(greater("123", "120"))
//console.log(greater_or_equal("12345", "12345"))
//console.log(long_sub("12", "2") == "10")
//console.log(long_sub("123456780", "2"),"123456778")
//console.log(long_sub("10000", "9") == "9991")
//console.log(long_sub("9", "10000"), "-9991")
//console.log(long_div("126", "21"), "12/2")
//console.log(long_div("4999999999999061959355493615493617043615249286192", "2"))
//console.log(long_div("2499999999999530979677746807746808521807624643096", "2"))
//console.log(bin("20"))
//console.log('add', long_add("010" , "10"))
//console.log('mul: ', long_mul("001", "123")) //13121232343453245", "3432434534234532412"))
//for (var i = 0; i < 65536; i++)
//	console.log(i, bin(i.toString()) == i.toString(2))
//console.log(bin("9999999999998123918710987230987234087230498572384977777777777123234872324736982734593247539284"))
//console.log(isqrt("1231111111111111111111111123423453456456756767823423423421312234324545645732434654656765"))
//console.log(isqrt("23232328323215435345345345343458098856756556809400840980980980980809092343243243243243098799634"))
//for (var i = 0; i < 656536; i++)
//	if (isqrt(i.toString()) != Math.floor(Math.sqrt(i)).toString())
//		console.log(i)
//console.log(long_mul('123111111111111111111111111232345345345', '123111111111111111111111111232345345345'))
console.log('done')
var r1 = '1234567890'
var r2 = '123345567723141342345245634565467678789070'

const multiply = (a,b,c=0) => [...a].reverse()
  .map((d,i,m) => (v = d*b+c , i == m.length-1 ? v : ( c = ~~(v/10) , v%10 ) ) )
    .reverse().join``.replace(/^0+/,'') || '0'

//console.log(multiply(r1, r2))
//console.log([...r1].reverse().map((d,i,m) => d*r2))
//console.log([...r1], r2 * 30)
