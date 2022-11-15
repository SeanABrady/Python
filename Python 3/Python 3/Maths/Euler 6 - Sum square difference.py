sumOfSquares = 0
squareOfSum = 0

for i in range(1,101):
    sumOfSquares += i ** 2

for i in range(1, 101):
    squareOfSum += i

squareOfSum = squareOfSum ** 2

print(squareOfSum - sumOfSquares)
