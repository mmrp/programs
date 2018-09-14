
hn = 143;
while 1:
	s = 2 * hn * (2 * hn - 1);
	pn = hn+1;
	while 1:
		p = pn * (3 * pn - 1);	
		if (p > s):
			break;
		if (s == p):
			n = pn+1;
			print "p:", pn, "\n"
			while 1:
				l = n * (n + 1);
				if (l > p):
					break;
				if (p == l):
					print n, pn, hn;
				n += 1;
		pn += 1;
	hn += 1;
#	print hn, "\n";

