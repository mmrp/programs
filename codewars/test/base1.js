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
primes = [2, 3, 5, 7, 11, 13, 17, 19]
function find_primes(N) {
	p = primes[primes.length-1]+2
	N = Math.ceil(Math.sqrt(N))
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
		p += 2
	}
	return primes
}

function mul_divisors(divisors, s, f)
{
	let i, j, k
	k = s + f
	for (j = f; j < s+f; j++)
		for	(i = 0; i < f; i++)
			divisors[k++] = divisors[j] * divisors[i]
	return k
}


function find_divisors(n) {
	find_primes(n)
	console.log('primes done')
	let divisors = new Array(1000)
	let f = 0
	let p = 1
	let l = 0
	let s = 0
	let prod = 1
	while (p*p < n) {
		p = primes[l++]
		prod = 1
		s = 0
		while (n % p == 0)  {
			n = n/p
			prod *= p
			divisors[f + s] = prod
			s++
		}
		f = mul_divisors(divisors, s, f)
	}
	if (n > 1) {
		divisors[f+s] = n
		s++
		f = mul_divisors(divisors, s, f)
	}
    divisors = divisors.sort(function (a, b) { return a - b;})
    return divisors
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
    return valid_number(n, find_divisors(n-1))
}
//console.log(find_primes(1000))
console.log(find_divisors(4562421213421341))
