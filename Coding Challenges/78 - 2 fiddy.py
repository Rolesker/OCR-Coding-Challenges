#i know that the challenge was to output the exact combinations, but run the code and you will see why that wasn't really sensible, this is how many unique combos there are

standard_coins=[1,2,5,10,20,50,100,200] #in pence
target=250

def coin_change(amount, coins):
    cache={}

    def dfs(i,a):
        if a==amount:
            return 1
        if a>amount:
            return 0
        if i==len(coins):
            return 0
        if (i,a) in cache:
            return cache[(i,a)]
        cache[(i,a)]=dfs(i,a+coins[i])+dfs(i+1,a)
        return cache[(i,a)]
    return dfs(0,0)


print(coin_change(target,standard_coins))