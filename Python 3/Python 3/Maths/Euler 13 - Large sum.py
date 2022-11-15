numberArray = []

with open("numbers.txt", "r") as numbers:
    for number in numbers:
        currentNumbers = number.split("/n")
        for number in currentNumbers:
            numberArray.append(number)

total = 0

for number in numberArray:
    print(number)
    total += int(number)

print(str(total))

