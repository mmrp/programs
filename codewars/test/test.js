function primeFactorList(n) {
	if (n < 1)
		throw "Argument error";
	var result = [];
	while (n != 1) {
		var factor = smallestFactor(n);
		result.push(factor);
		n /= factor;
	}
	return result;
}


/* 
 * Returns the smallest prime factor of the given integer.
 * Examples:
 * - smallestFactor(2) = 2.
 * - smallestFactor(15) = 3.
 */
function smallestFactor(n) {
	if (n < 2)
		throw "Argument error";
	if (n % 2 == 0)
		return 2;
	var end = Math.floor(Math.sqrt(n));
	for (var i = 3; i <= end; i += 2) {
		if (n % i == 0)
			return i;
	}
	return n;
}

//console.log(primeFactorList())

console.log(primeFactorList(4562421213421341))
