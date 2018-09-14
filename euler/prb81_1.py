with open("jump", "r") as f:
        s = [[int(x) for x in line.split()] for line in f]

#print s;


size=8;
cost=[[0 for row in range(size)] for col in range(size)];

cost[0][0] =  s[0][0];

print s[size-1][size-1];
print s;

for r in range(1, size):
	cost[r][0] = cost[r-1][0] + s[r][0];

for c in range(1, size):
	cost[0][c] = cost[0][c-1] + s[0][c];
	
for r in range(1, size):
	for c in range(1, size):
		cost[r][c] = s[r][c] + min(cost[r-1][c], cost[r][c-1]);

print cost[r][c];
#tracing back
tcost = cost[r][c];
r = size-1;
c = size-1;
while tcost > 0 and r >= 1 and c >= 1:
	tcost -= s[r][c];
	print r, c;
	if (cost[r-1][c] < cost[r][c-1]):
		r = r-1;
	else:
		c = c-1;	


if r == 0:
	while (tcost > 0):
		tcost -= s[r][c];
		c = c - 1;
		print r, c;
			
else:
	while (tcost > 0):
		tcost -= s[r][c];
		r = r - 1;	
		print r, c;

