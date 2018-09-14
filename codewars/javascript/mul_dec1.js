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

function maxorder(n1, n2) {
	if (lte(n1, n2)) 
		return [n2, n1]
	else 
		return [n1, n2]
}

function trim(a) {
	if (a.indexOf('.') != -1) {
		var p1 = a.replace(/\.\d*/,'').replace(/^0+/,'')
		var p2 = a.replace(/\d*\./,'').replace(/0+$/,'')
		return [p1 + p2, p2.length]
	}
	return [a, 0]
}

function add2(a, b, c = 0) {
	[a, b] = [a, b].map(v => v.split("").map(v => parseInt(v)))
	let s;
	let res = ''
	while (a.length || b.length || c) {
		s = ~~a.pop() + ~~b.pop() + c
		c = ~~(s/10)
		res = (s % 10) + res
	}
	return res
	//return res.replace(/^0+/,'') || '0'
}

function add1(a, b, c = 0) {
	[a, b]  = maxorder(a, b).map(v => v.split("").map(s => parseInt(s)).reverse())
	let res = ''
	for (var i = 0; i < a.length; i++) {
		let s = c + a[i] + (b[i]||0)
		c = ~~(s/10)
		res = (s % 10) + res
	}
	if (c) res = c + res	
	return res
	return res.replace(/^0+/,'') || '0'
}



function mul(a, b) {
	let neg = ((a[0] == '-') ^ (b[0] == '-')) ? '-' : ''
	let dotlen = ((a.indexOf('.') == -1) ? 0: (a.length - a.indexOf('.') - 1))  
	dotlen	+=   ((b.indexOf('.') == -1) ? 0: (b.length - b.indexOf('.') - 1))
	a = a.replace(/\-|\./g,'').split("").reverse()
	b = b.replace(/\-|\./g,'').split("").reverse()
	const res = []
	for (let i = 0; i < a.length; i++) {
		for (let j = 0; j < b.length; j++) {
			res[i+j]? res[i+j] += a[i] * b[j]:  res[i+j] = a[i] * b[j]
			res[i+j+1] = ~~(res[i+j] / 10) + (res[i+j+1] || 0)
			res[i+j] %= 10
		}
	}
	if (dotlen) res.splice(res.length - dotlen, 0, '.')
	let out = res.join('').replace(/\.(\d*[1-9])?0+$/, '.$1').replace(/^0+|\.$/g,'').replace(/^\./, '0.')
	return (!out) ? '0' : neg + out
}

function multiply(n, o){
  let prefix = /^\-/.test(n) + /^\-/.test(o) === 1 ? '-' : '';
  let dotIndex = (n.indexOf('.') === -1 ? 0 : (n.length - n.indexOf('.') - 1)) + (o.indexOf('.') === -1 ? 0 : (o.length - o.indexOf('.') - 1));
  o = o.replace(/\-|\./g,'').split('').reverse();
  n = n.replace(/\-|\./g,'').split('').reverse();
  const resArr = [];
  for (let i = 0; i < o.length; i ++) {
    for(let j = 0; j < n.length; j ++) {
      resArr[i + j] ? resArr[i + j] += o[i] * n[j] : resArr[i + j] = o[i] * n[j];
      resArr[i + j + 1] = Math.floor(resArr[i + j] / 10) + (resArr[i + j + 1] || 0);
      resArr[i + j] = resArr[i + j] % 10;
    }
  }
  let res = resArr.reverse();
	console.log(res)
  if (dotIndex) res.splice(res.length - dotIndex, 0 , '.');
  res = res.join('').replace(/\.(\d*[1-9])?(0+)$/,'.$1').replace(/\.$|^0+/g,'').replace(/^\./, '0.');
  return (res === '0' || !res) ? '0' : prefix + res;
}

console.log(add2('123', '345') == '468')
console.log(add2('1230', '0345') == '1575')
console.log(add2('123423459830982374077543409368907240', '72013847034787234097823454563459643589634') == '72013970458247065080197532106869012496874')
console.log(mul("1234567990012345", "1234567899542334"))
console.log(mul("123.4567990012345", "123456789954233.4"))
console.log(mul("2.0", ".5"))
console.log(mul("2.0000", "1000.05"))
console.log(mul('0.0', '0.0'))
//console.log("1234")
