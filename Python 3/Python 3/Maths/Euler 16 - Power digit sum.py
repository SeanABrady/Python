number = 2 ** 1000
total = 0

for digit in str(number):
    total += int(digit)

print(total)
