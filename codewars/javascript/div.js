function long_div(a, b)
{
	a = a.replace(/^0+/, '')
	b = b.replace(/^0+/, '')
	if (lt(a, b)) return ['0', a]

	a = a.split("")
	let acc = a.shift() 
	while (lt(acc, b) && a.length)
		acc += a.shift()

	let quotient = ''
	let q;
	for (q = 0; lte(b, acc); q++) {
		acc = sub(acc, b)
	}

	quotient += q.toString()
	while (a.length) {
		let j = a.length
		while (lt(acc, b) && a.length) 
			acc += a.shift()
		if (j > a.length)	
			quotient += '0'.repeat(j - a.length - 1)
		
		if (lt(acc, b)) {
			quotient += '0'
			break
		}
		
		for (q = 0; lte(b, acc); q++) 
			acc = sub(acc, b)

		quotient += q.toString()
	}
	return [quotient, acc.replace(/^0+/, '')||'0']
}

//assuming no zero's prepended to n1 or n2
function lt(n1, n2) {
	n1 = n1.replace(/^0+/, '')
	n2 = n2.replace(/^0+/, '')
	return (n1.length < n2.length) || (n1.length == n2.length &&
		   ([...n1].map((v, i) => v - n2[i]).find(e => e != 0) < 0))
}

function lte(n1, n2) {
	n1 = n1.replace(/^0+/, '')
	n2 = n2.replace(/^0+/, '')
	return n1 == n2	|| lt(n1, n2)
}

function gt(n1, n2) {
	return !lte(n1, n2)
}

//assumption a >= b
function sub(a, b) {
//	console.log(typeof(a), typeof(b))
	a = a.replace(/^0+/,'').split("")
	b = b.replace(/^0+/,'').split("")
	let res = '' 
	while (a.length) {
		let s = (~~a.pop()) - (~~b.pop())
		if (s < 0) {
			s += 10
			a[a.length-1]--
		}
		res = s + res;
	}
	return res.replace(/^0+/,'') || '0'
}
//console.log(sub('1000', '100'))
//console.log(lt('19', '1042'))
//console.log(mul('123454', '123234234') , '123454' * '123234234')
console.log(long_div('201', '2'))
for (let p = 0; p < 100000; p++) {
	if (long_div(p.toString(), '122342')[0] != ~~(p.toString() / '1223422')) {
		console.log('failed', p, long_div(p.toString(), '122342'))
	}
}


  function divideStrings(a,b) {
  if(!strvalcmp(a, b)) return ['0',a];
  var quo = '', len = a.length-b.length, rem = a.slice(0,b.length);
  a = a.slice(b.length);
  for(let i=0; i<=len; i++) {
    var dgt = 0;
    for(;strvalcmp(rem,b);dgt++) rem = subtractStrings(rem,b);
    quo=(quo==='0'?'':quo)+dgt;
    rem=(rem==='0'?'':rem)+(a[0]||'');
    a=a&&a.slice(1);
  }
  return [quo+a,rem||'0'];
}
var strvalcmp=(a,b)=>a.length>b.length || (a.length===b.length && a>=b);
function subtractStrings(a, b) {
  if(a===b)return '0';
  var res = '', c = 0;
  a = a.split(''); b = b.split('');
  while (a.length || b.length || c) {
    c += ~~a.pop() - ~~b.pop();
    res = (c+10) % 10 + res;
    c = -(c < 0);
  }
  return res.replace(/^0+/, '');
}
console.log(long_div('123234949889428942982498982439082349804123234949889428942982498982439082349804239423942994948982348948948423232323232323232323232323232323232323232323232323232323232323232323232323884323478923774832423884328432763167267398897478547637318938318938123873781731371763214631371763147321783128312', '1324718799999999999999999999999999932167231498237459876234794597234629473679856197836497326789643963259') , '93027252190750929919994328184277566012149511393123494582299921651205639799716092457034375713670484696543990074642769473574815742506000729769012517924')
