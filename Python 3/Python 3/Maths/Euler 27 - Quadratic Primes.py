def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

sequence = 0

for a in range(-2000,2000):
    for b in range(-2000,2000):
        consecutive = True
        n = 0
        while consecutive == True:
            possiblePrime = n**2 + a*n + b
            if is_prime(possiblePrime) == False:
                consecutive = False
                n = 0
            else:
                n += 1
                if n > sequence:
                    sequence = n
        
print(sequence)
        

