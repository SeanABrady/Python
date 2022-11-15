inputNumber = int(raw_input("Enter a number "))

counterEven = 0
counterOdd = 0
currentNumber = inputNumber
while currentNumber != 1:
    if currentNumber % 2 == 0:
        currentNumber = currentNumber / 2
        print currentNumber
        counterEven += 1
    else:
        currentNumber = currentNumber * 3 + 1
        print currentNumber
        counterOdd += 1

print "This took %d steps" % (counterEven + counterOdd)
print "It increased %d times and decreased %d times" % (counterOdd, counterEven)
