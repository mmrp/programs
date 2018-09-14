def base2(n):
	s="";#[0 for i in range (30)];
	i = 0;
	while n:
		s += str(n%2);
		n = n /2;
		i += 1;
	return s;


print base2(100);
	
s = "hello" + "worl";
print s
