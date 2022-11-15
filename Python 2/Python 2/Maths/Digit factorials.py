import math
total = 0
numbers = []
for i in range(3,2540162):
    for char in str(i):
        total += math.factorial(int(char))
    if total == i:
        numbers.append(i)
        total = 0
    else:
        total = 0

print numbers
print sum(numbers)
