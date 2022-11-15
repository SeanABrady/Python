numbers = []
for i in range(10,4251529):
    total = 0
    for char in str(i):
        total += int(char) ** 6
    if total == i:
        numbers.append(i)

print numbers
print sum(numbers)

