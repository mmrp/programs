function calculate(str) {
	numbers = str.split(/[*+$-]/).map(v=>parseFloat(v))
	operators = str.match(/[*+$-]/g) || []
	prec = {'+': 1, '-': 2, '*': 3, '$': 4, '(': -1}
	output = []
	opr = []
	operators.push('(')
	console.log(numbers)
	if (str.replace(/[0-9.+-*$]/g,''))
		return 'Bad request'

	while (numbers.length) {
		output.push(numbers.shift())
		incoming_op = operators.shift()
		top_op = opr[opr.length-1]
		while (opr.length && (prec[top_op] >= prec[incoming_op])) {
			output.push(opr.pop())
			top_op = opr[opr.length-1] || '0'
		}
		opr.push(incoming_op)
		//console.log(output)
	}
	while (opr.length > 1) {
		output.push(opr.pop())
	}
	console.log(output)
	val = []
	while (output.length) {
		e = output.shift()
		if (!prec[e]) {
			val.push(e)
			continue;
		}
		e2 = val.pop()
		e1 = val.pop()
		if (e == '+')
			v = e1 + e2
		else if (e == '-')
			v = e1 - e2
		else if (e == '*')
			v = e1 * e2
		else if (e == '$')
			v = e1 / e2
		val.push(v)
    }
	return val.pop()
}
console.log(calculate("5-5-5-5"))
