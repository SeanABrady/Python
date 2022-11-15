##factors = []
##triangle = 1
##i = 1
##maxFactors = 0
##
##
##while i < 10000000000:
##    triangle += i
##    factors.append(triangle)
##    factors.append(1)
##    for j in range(2, triangle // 2 + 1):
##        if triangle % j == 0:
##            factors.append(j)
##        if len(factors) > 500:
##            print(triangle, len(factors))
##            break
##        if len(factors) > maxFactors:
##            maxFactors = len(factors)
##            print(triangle, maxFactors)
##    factors = []
##    i += 1000

import math
from time import time
t = time()
def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            number_of_factors +=2
        if i*i==n:
            number_of_factors -=1
    return number_of_factors


for n in range(1,1000000):
    triangleNumber = (n*(n+1))/2
    if n%2==0:
        cnt=divisors(n/2)*divisors(n+1)
    else:
        cnt=divisors(n)*divisors((n+1)/2)
    if cnt >= 500:
        print(triangleNumber)
        break

tt = time()-t
print(tt)
