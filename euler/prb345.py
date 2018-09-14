with open("data", "r") as f:
	s=[[int(r) for r in line.split()] for line in f];

print s;



def find_max(r, c):
