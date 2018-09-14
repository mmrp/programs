#!/usr/bin/python


import sys
"""
   0  1  2  3  4
0  0  0  0  0  0
1  0  1  1  1  1
2  0  1  2  2  3
3  0  1  2  3  4 
"""
def make_change(coins, n):
    coins = [0] + coins
    d = [[0 for i in range(n+1)] for j in range(len(coins))]
    print(d)
    #return
    for i in range(1, len(coins)):
        for j in range(1, n+1):
            for k in range(0, j//coins[i]+1):
                d[i][j] += d[i-1][j - k * coins[i]]
            if j % coins[i] == 0:
                d[i][j] += 1
            #print(d)

    print(d)
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))

