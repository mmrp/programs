


def comb(carr, n, r):
	if carr[n][r] != -1:
		return carr[n][r];
		
	carr[n][r] = comb(carr, n-1, r-1) + comb(carr, n-1, r);
	return carr[n][r];


carr=[[-1 for col in range (101)]  for row in range (101)];

for i in range(0,101):
	carr[i][0] = 1;
	carr[i][1] = i;

for j in range(0,101):
	carr[0][j] = 0;

count=0;
for i in range(1,101):
	for j in range(2,101):
		if carr[i][j] == -1:
			carr[i][j] = comb(carr, i,j); 
		if  (carr[i][j] > 1000000):
			count += 1;
print carr
print count;
