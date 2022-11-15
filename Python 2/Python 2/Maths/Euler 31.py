#Project Euler Problem 31

target = 44
coins = [4, 6, 10, 20]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]
        
print "Ways to make change =", ways[target]


