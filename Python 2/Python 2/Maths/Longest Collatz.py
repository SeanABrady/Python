inputNumber = int(raw_input("Enter a number "))
numberSteps = 0
number = 0
counter = 0


for i in range(1,inputNumber + 1):
    currentNumber = i
    while currentNumber != 1:
        if currentNumber % 2 == 0:
            referenceNumber = currentNumber
            currentNumber = currentNumber / 2
            counter += 1
        else:
            referenceNumber = currentNumber
            currentNumber = currentNumber * 3 + 1
            counter += 1
    if currentNumber == 1:
        if counter > numberSteps:
            numberSteps = counter
            counter = 0
            number = i
        else:
            counter = 0

            

#print numberSteps
#print number
print "The max number of steps taken was", numberSteps,
print "for the number", number
