

def is_palindrome_2(n):
	s ="";
	j = n;
	while j:
		s += str(j%2);
		j = j/2;
	s1 = s;
	return s == s1[::-1];
	
def is_palindrome(n):
	return  str(n) == (str(n)[::-1]);


sum = 0;
for i in range(1, 1000000):
	if is_palindrome(i) and is_palindrome_2(i):	
		print i, "\n";
		sum += i;

print sum;
