import math
from decimal import Decimal
numPeople = int(raw_input("Enter a number of people "))

#noUnique = (math.factorial(365) / (365 ** numPeople * math.factorial(365 - numPeople))) * 100
combinations = Decimal(math.factorial(365))
chances = Decimal(365 ** int(numPeople))
factorial = Decimal(math.factorial(365 - int(numPeople)))

noCommon = (combinations / (chances * factorial))
commonBirthday = (1 - noCommon) * 100

print "The probability of %d people having at lease one common birthday is %.6f%%" % (numPeople, commonBirthday)
