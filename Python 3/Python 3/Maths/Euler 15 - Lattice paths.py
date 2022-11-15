##import math
##
##def lattice(n, k):
##    nfact = math.factorial(n + k)
##    kfact = math.factorial(k)
##    return (nfact/(kfact*math.factorial(n-k)))
##
##print(lattice(20,20))

import math

def pe15(n):
    n_fact = math.factorial(n)
    return math.factorial(2 * n) / n_fact / n_fact

print(pe15(20))
