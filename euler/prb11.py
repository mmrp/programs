with open("11.d") as f:
        s = [[int(x) for x in line.split()] for line in f]

#find in row, max sum
maxsum = 0;
row=0;
col=0;
ind=0;
for r in  range(20):		#row
	for c in range(20-3):	#col
		sum = s[r][c] * s[r][c+1] * s[r][c+2] * s[r][c+3];
		if (sum > maxsum):
			maxsum = sum;
			row=r;
			col=c;
			ind=1;

#find in col, max sum
for c in range(20):		#col
	for r in  range(20-3): 	#row
		sum = s[r][c] * s[r+1][c] * s[r+2][c] * s[r+3][c];
		if (sum > maxsum):
			maxsum = sum;
			row=r;
			col=c;
			ind=2;
		

#find in top diagnaol, max sum
for d in range(0 , 20-3):		
		r = 0;
		c = d;
		while (c < (20- 3)):
			sum = s[r][c] * s[r+1][c+1] * s[r+2][c+2] * s[r+3][c+3];
			if (sum > maxsum):
				maxsum = sum;
				row=r;
				col=c;
				ind=3;
			r = r + 1;
			c = c + 1;

#find in bottom diagnaol, max sum
for d in range(0, 20-3):		
		c = 0;
		r = d;
		while (r < (20-3)):
			sum = s[r][c] * s[r+1][c+1] * s[r+2][c+2] * s[r+3][c+3];
			if (sum > maxsum):
				maxsum = sum;
				row=r;
				col=c;
				ind=4;
			r = r + 1;
			c = c + 1;


#find in bottom diagnaol, max sum
for d in range(0, 20-3):		
		r = 19;
		c = d;
		while (c < (20- 3)):
			sum = s[r][c] * s[r-1][c+1] * s[r-2][c+2] * s[r-3][c+3];
			if (sum > maxsum):
				maxsum = sum;
				row=r;
				col=c;
				ind=3;
			r = r - 1;
			c = c + 1;

#find in bottom diagnaol, max sum
for d in range(19, 3, -1):		
		c = 0;
		r = d;
		while (r > 3):
			sum = s[r][c] * s[r-1][c+1] * s[r-2][c+2] * s[r-3][c+3];
			if (sum > maxsum):
				maxsum = sum;
				row=r;
				col=c;
				ind=4;
			r = r - 1;
			c = c + 1;




print maxsum;
print row;
print col;
print ind;
