


def reverse(n):
	return int(str(n)[::-1]);
	
def is_palindrome(n):
	if reverse(n) == n:
		return 1;
	return 0;
	
	

tlen=0;
prd=0;
tprd=0;
for i in range(999,100, -1):
	for j in range(999, 100, -1):
		tprd = i * j;
		if is_palindrome(tprd):
			if tprd > prd:
				prd = tprd;
				print i, j, prd;
