
def fact(x):
	return (1  if 	x==0  else x * fact(x-1))


if (len(sys.argv)):
	print fact(int(sys.argv[1]))
else:
	print "fact.py"
