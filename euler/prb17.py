#!/usr/bin/python
numbers=[0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3,\
	    6, 6, 8, 8, 7, 7, 9, 8, 8, 6]
for i in range(21, 1001):
	numbers.append(0)
numbers[30] = 6
numbers[40] = 6
numbers[50] = 5 
numbers[60] = 5 
numbers[70] = 7 
numbers[80] = 6 
numbers[90] = 5 
numbers[100] = 10 
base = 20
for i in range(21, 100):
	if i % 10 == 0:
		base += 10
		continue
	numbers[i] = numbers[base] + numbers[i%10]
base1 = numbers[1]
for i in range(101, 1000):
	if i % 100 == 0:
		base1 = numbers[i/100] 
		numbers[i] = base1 + 7
	else:
		numbers[i] = base1 +  7 + 3 + numbers[i%100]
numbers[1000] = 3 + 8
print numbers
print sum(numbers)
print len(numbers)

