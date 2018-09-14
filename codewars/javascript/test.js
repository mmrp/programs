function solveExpression(exp) {
  let str='9876543210'
  for (let i = 0; i < str.length; i++) {
    let e = exp.replace(/\?/g, str[i])
    e = e.replace('=','==')
	console.log(e, eval(e))
	let d = e.match(/\d+/g)
	let ok = true
	for (let j = 0; j < d.length; j++) {
		if (d[i].length > 1 && d[i][0] =='0') {
			okay = false
			break
		}
	}
    if (ok && eval(e))
      return parseInt(str[i])
  }
}
console.log(solveExpression('3?1+1=3??'))
