function valid_number(n, divisors) {
    //#print(n, divisors)
    console.log(n, divisors)
    for (let i = 0; i < divisors.length; i++) { //p in divisors:
        p = divisors[i];
        let v = Math.log((((n-1)*(p-1)/p)+1))/Math.log(p)
        console.log(v)
        if (Math.ceil(v) - v < 0.0000001)
            return p
    }
    return -1
}
function find_primes(N) {
	let primes = [2, 3, 5, 7, 11, 13, 17, 19]
	p = primes[primes.length-1]+1
	while (p < N) {
		let l = Math.ceil(Math.sqrt(p))
		let isprime = true 
		for (let i = 0; primes[i] <= l; i++) {
			if (p % primes[i] == 0) {
				isprime = false
				break
			}
		}
		if (isprime)
			primes.push(p)
		p++
	}
	return primes

}


function get_divisors(n) {
    let m = parseInt(Math.sqrt(n))+1
    let l = m
    let s = 3
    if (n % 2 == 0)
      s = 2 
    let divisors = []
    while (s < l) {
        if (n % s == 0) {
            c = Math.floor(n/s)
            divisors.push(s)
            if (c != s)
                divisors.push(c)
            console.log(s, c)

            l = c 
        }
        s += 2;
    }
    divisors.push(n)
    divisors = divisors.sort(function (a, b) { return a - b;})
    //console.log(divisors)
    return divisors
}

function getMinBase(n) {
    return valid_number(n, get_divisors(n-1))
}
console.log(find_primes(1000))
