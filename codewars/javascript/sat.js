function prep1(str, repeat = 0) {
	var arr = []
	if (repeat == 1) return str;
	for (var i = 0; i < str.length; i++) {
		var tmp = prep(str, repeat-1);
		for (var j = 0; j < tmp.length; j++) 
			arr.push(str[i] + tmp[j])
	}
	return arr
}

function product(str, repeat = 0) {
	var arr = []
	if (repeat == 1) { 
		for (var i = 0; i < str.length; i++)
			arr.push([str[i]])
		return arr
	}

	for (var i = 0; i < str.length; i++) {
		var tmp = product(str, repeat-1);
		for (var j = 0; j < tmp.length; j++) 
			arr.push([str[i]].concat(tmp[j]))
	}
	return arr
}

function permutation(arr) {
	if (arr.length == 1)  return [[arr[0]]]

	var narr = []
	for (var i = 0; i < arr.length; i++) {
		t = arr[0]
		arr[0] = arr[i]
		arr[i] = t
		var tmp = permutation(arr.slice(1))
		for (var j = 0; j < tmp.length; j++)
			narr.push([arr[0]].concat(tmp[j]))
		t = arr[0]
		arr[0] = arr[i]
		arr[i] = t
	}
	return narr
}
		

function equalTo24(a,b,c,d){
	console.log ([a.toString(), b.toString(), c.toString(), d.toString()], 4)
	nums  = permutation([a.toString(), b.toString(), c.toString(), d.toString()])
	console.log(nums)
	opers = product(['+', '-', '/', '*'], 3)
	for (var i = 0; i < nums.length; i++) {
			n = nums[i]
			console.log(n)
		for (var j = 0; j < opers.length; j++) {
			o = opers[j]
  			e1 = '(' + n[0] + o[0] + n[1] + ')' + o[1] + '(' + n[2] + o[2] + n[3] + ')'
			e2 = '(' + '(' + n[0] + o[0] + n[1] + ')' + o[1] + n[2] + ')' + o[2] + '(' + n[3] + ')'
		  	e3 = '(' + '(' + n[0] + ')' + o[0] + '(' + n[1] +  o[1] + n[2] + ')' + ')' + o[2] + '(' + n[3] + ')'
	 		e4 = '(' + n[0] + ')' + o[0] + '(' + n[1] +  o[1] + '(' + n[2] + o[2] + n[3] + ')' + ')' 
 			e5 = '(' + n[0] + ')' + o[0] + '(' + '('  + n[1] +  o[1] + n[2] + ')' + o[2] + n[3] + ')'  	
			if (eval(e1) == 24) 
				return e1
			if (eval(e2) == 24) 
				return e2
			if (eval(e3) == 24) 
				return e3
			if (eval(e4) == 24) 
				return e4
			if (eval(e5) == 24) 
				return e5
//			console.log(e1, e2, e3, e4, e5)
		}
	}
}

//console.log(prep(['+', '/', '*', '-'], 2))
//console.log(prep(['+', '/', '*', '-'], 2))
//console.log(prep("112012", 3))
console.log(permutation([1,2,3,4]))
console.log(equalTo24(7, 12, 12, 10)) //1,2,3,4))
