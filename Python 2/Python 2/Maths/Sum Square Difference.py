totalInt = 0

for i in range(1,100):
    totalInt += i

squaresum = totalInt ** 2

sumsquare = 0

for i in range(1,100):
    sumsquare += i ** 2

print squaresum - sumsquare
