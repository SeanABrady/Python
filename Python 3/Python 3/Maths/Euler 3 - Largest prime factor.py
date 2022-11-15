from functools import reduce
from math import sqrt

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if not n % i)))

print(factors(14))




