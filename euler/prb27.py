import math;

def prime(n1):
	if (n1 < 0):
		return 0;
	max = int(math.sqrt(n1));
	for p in range(2, max):
		if n1 % p == 0:
			return 0;

	return 1;
		


def get_prime_count(a, b):
	n = 0;
	while 1:
		if not prime(n * n + a * n + b):
			break;
		n += 1;     
	return n;




max_primes = 0;
tmax_primes = 0;
for a in range(-999, 999):
	for b in range(-999, 999):
		tmax_primes = get_prime_count(a, b);		
		if (tmax_primes > max_primes): 
			max_primes = tmax_primes;
			prd = a * b;

print prd;
