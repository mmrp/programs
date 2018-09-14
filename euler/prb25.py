



f1=1;
f2=1;
term = 2;
while 1:
	f3 = f2 + f1;
	f1 = f2;
	f2 = f3;
	term += 1;
	if len(str(f3)) == 1000:
		break;

print term, f3;
