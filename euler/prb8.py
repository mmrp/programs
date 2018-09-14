r=open("d1", "r").read();
end = len(r)- 1 - 5;
prd = 0;
tprd = 0;
for i in range(0, end):
	tprd = int(r[i]) * int(r[i+1]) * int(r[i+2]) * int(r[i+3]) * int(r[i+4]); 	
	if tprd > prd:
		prd = tprd;

print prd;
 
