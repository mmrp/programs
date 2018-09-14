#!/usr/bin/python

def power_tower(nums):
    if len(nums) == 0: return 1
   
    if nums[-1] == 0:
        nums.pop()
        nums[-1] = 1
   
    if len(nums) == 1: return nums[0]
    i = len(nums)-2
    while i >= 0:
        if nums[i] == 0:
            nums[i] = nums[i]**nums[i+1]
        elif nums[i+1] == 0:
            nums[i] = 1
        i -= 1

    if len(nums) == 2:
        nums += [1]
    print(nums)

    a = nums[0]
    b = nums[1]
    c = nums[2]
    r1 = a % 2
    if a % 5 != 0:
        r2 = b % 4
        if r2 == 2 and c >= 2:
            r2 = 0
        elif r2 == 3:
            r2 = 3**(c % 2)
        r2 = (a**r2) % 5
    else:
        r2 = 0
    # chineese remainder theorem 10 = 2 * 5
    # solve power % 2 and power % 5 and solve the equation
 
    # find n such that it returns r1 when n % 2 and r2 when n % 5
    # 2 * x + r1 = n
    # 5 * y + r2 = n
    print(r1, r2)
    for i in range(5):
        if (2 * i + r1 - r2) % 5 == 0:
            return 2 * i + r1

import sys
print(power_tower([2, 0, 1]))
sys.exit(0)
print(power_tower([2, 2, 2, 0]) ==  4)
print(power_tower([3,3,5,4]))
print(power_tower([3,4, 2]))
print(power_tower([7, 6, 21]))
print(power_tower([4, 3, 6]) == 4)
print(power_tower([12, 30, 21]))
print(power_tower([937640,767456,981242]))
print(power_tower([]         ) ==  1);
print(power_tower([0,0]      ) ==  1); #0 ^ 0
print(power_tower([0,0,0]    ) ==  0); # 0^(0 ^ 0) = 0^1 = 0
print(power_tower([1,2]      ) ==  1);
print(power_tower([3,4,5]    ) ==  1);
print(power_tower([4,3,6]    ) ==  4);
print(power_tower([7,6,21]   ) ==  1);
print(power_tower([12,30,21] ) ==  6);
print(power_tower([2,2,2,0]  ) ==  4);
print(power_tower([937640,767456,981242] ) ,  0);
print(power_tower([123232,694022,140249] ) ==  6);
print(power_tower([499942,898102,846073] ) ==  6);

sys.exit(0)
