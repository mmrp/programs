


def cal_int_partition(arr, k, n):
	
	if arr[k][n] != -1:
		return arr[k][n];	
	
	arr[k][n] =   cal_int_partition(arr, k+1, n) + cal_int_partition(arr, k, n - k);
	return arr[k][n];		
		


size = 2000;
arr=[[0 for col in  range(size)] for row in  range(size)];

for i in range (0, size):
	for j in range(0, size):
		arr[i][j] = -1;
		if i > j:
			arr[i][j] = 0;

		if i == j:
			arr[i][j] = 1;


cal_int_partition(arr, 1, size-1);

for i in range(0, size):
	if (arr[1][i] % 1000000 == 0) :
		print i, arr[1][i], "\n";		

