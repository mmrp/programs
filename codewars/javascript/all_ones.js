function valid_number(n, divisors) {
    for (let i = 0; i < divisors.length; i++) { //p in divisors:
        p = divisors[i];
        let v = Math.log((((n-1)*(p-1)/p)+1))/Math.log(p)
        if (Math.abs((Math.floor(v+0.5) - v)/v) < 0.00000001)
            return p
    }
    return -1
}

function smallest_factor(n) {
	if (n % 2 == 0)
		return 2
	
	var end = Math.floor(Math.sqrt(n))
	for (let i = 3; i <= end; i += 2) 
		if (n % i == 0)
			return i

	return n

}
function get_factors(n) {
	let factors = []
	while (n > 1) {
		p = smallest_factor(n)
		factors.push(p)
		n = n/p
	}
    return factors
}

function get_divisors(n) {
	let factors = get_factors(n)
	let divisors = []

	for (let i = 0; i < factors.length; i++) {
		divisors.push(factors[i])
	l = divisors.length
		for (let j = 0; j < l; j++)
			divisors.push(factors[i] * divisors[j])
	}
	return Array.from(new Set(divisors.concat(factors))).sort(function (a, b) { return a - b;})
}

function getMinBase(n) {
    return valid_number(n, get_divisors(n-1))
}
