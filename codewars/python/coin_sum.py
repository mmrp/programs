def count_change(money, coins):
    #print money, coins

    return change(money, sorted(coins))

def change(money, coins):  
    if money == 0:
        return 1
    cnt = 0
    for p, c in enumerate(coins):
        if c > money:
            break
        #print money, c
        cnt += count_change(money - c, coins[p:])
         #print cnt
    return cnt       
    # your implementation here
