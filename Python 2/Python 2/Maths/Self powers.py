total = 0
for i in range(1,1001):
    total += i ** i

strTotal = str(total)
finalTenReverse = strTotal[-10:]

print finalTenReverse
