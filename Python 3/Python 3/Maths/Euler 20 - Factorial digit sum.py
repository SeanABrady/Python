import math

total = 0

number = str(math.factorial(100))

for digit in number:
    total += int(digit)

print(total)

