inputNumber = int(raw_input("Enter a number to find its prime factors "))

factors = []

for i in range(1, inputNumber):
    if inputNumber % i == 0:
        factors.append(i)

print factors


for i in range(1, (factors[len(factors) - 1])/2):
    for number in factors:
        if number % i == 0 and i != number and i != 1:
            factors.remove(number)
        

print factors
        

        
    
