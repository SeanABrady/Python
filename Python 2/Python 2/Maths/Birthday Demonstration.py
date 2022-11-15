from random import randint
from decimal import Decimal

counterTrue = 0
counterFalse = 0

userInput = int(raw_input("Choose a number of random birthdays to generate "))
for j in range(1, 5001):
    found = False
    birthdays = []

    for i in range(1, userInput + 1):
        birthdays.append(randint(1,366))

    birthdays.sort()

    for i in range(birthdays[0],birthdays[len(birthdays) - 1] - 1):
        if birthdays.count(i) >= 2:
            found = True
            counterTrue += 1
            break

    if found == False:
        counterFalse += 1

share = Decimal(counterTrue)
noshare = Decimal(counterFalse)

print "Of 5000, the percentage of cases with at least one shared birthday is", share/(share+noshare) * 100, "%"
