primeCheck = 4
#found = False
counter = 0
checker = 2
primes = [2,3]

while counter < 100:
    while checker <= primeCheck:
        if primeCheck % checker == 0:
            primeCheck += 1
            checker += 1
            counter += 1
        else:
            checker += 1
            counter += 1
            
print primeCheck
                
