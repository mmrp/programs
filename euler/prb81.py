with open("jump", "r") as f:
        s = [[int(x) for x in line.split()] for line in f]

#print s;

#!/usr/bin/python
size=8;
cost=[[0 for row in range(size)] for col in range(size)];

cost[0][0] =  s[0][0];


for r in range(1, size):
	s[r][0] = s[r-1][0] + s[r][0];

for c in range(1, size):
	s[0][c] = s[0][c-1] + s[0][c];
	
for r in range(1, size):
	print r+1, 1, s[r][0], " ";
	for c in range(1, size):
		print min(s[r-1][c], s[r][c-1]);
		s[r][c] = s[r][c] + min(s[r-1][c], s[r][c-1]);
		print r+1, c+1, s[r][c], " ";
	print "\n";

