with open("67.d") as f:
	no_lines = [int(x) for x in f.readline().split()]
	s = [[int(x) for x in line.split()] for line in f]

for i in range(1, no_lines[0]):
	j = 0;
	s[i][j] += s[i-1][j];	
	j += 1;
	while j < i:
		if (s[i-1][j] > s[i-1][j-1]):
			s[i][j] += s[i-1][j];
		else:
			s[i][j] += s[i-1][j-1];
		j += 1;

	s[i][j] += s[i-1][j-1];	

i = no_lines[0]-1;
t = s[i][0];

for j in range(1, no_lines[0]):
	if (t < s[i][j]):
		t = s[i][j];
print t;
