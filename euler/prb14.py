def get_seq(n):

	loop = 1;
	while (n != 1) :
		if n%2 == 0:
			n = n/2;
		else:
			n = 3*n+1;
		loop = loop + 1;
	
	return loop;




tseq = 0;
fseq = 0;
fnum = 1;
for i in range(1000000):
	tseq = get_seq(i+1);
	if tseq > fseq:
		fseq = tseq;
		fnum = i+1;

print fnum;
