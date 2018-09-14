size=21;
arr=[[0 for col in  range(size)] for row in  range(size)];

for r in range(size):
	arr[r][0] = 1;	
for c in range(size):
	arr[0][c] = 1;

for r in range(1, size):
	for c in range(1, size):
		arr[r][c] = arr[r][c-1] + arr[r-1][c];


print arr[r][c];
		

