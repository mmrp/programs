



f1=1;
f2=2;
term = 2;
sum = f2;
while 1:
	f3 = f2 + f1;
	f1 = f2;
	f2 = f3;
	term += 1;
	if f3 > 4 * 1000 * 1000:
		break;
	if f3 % 2 == 0:
		sum += f3;

print sum;
