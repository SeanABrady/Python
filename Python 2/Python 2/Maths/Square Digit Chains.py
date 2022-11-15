inputNumber = int(raw_input("Enter a number "))
stringNumber = str(inputNumber)
newNumber = 0
numberCheck = []
finalNumberCheck = []

while int(stringNumber) not in finalNumberCheck:
    listNumber = []
    for digit in stringNumber:
        #print digit
        listNumber.append(int(digit) ** 2)
        #print listNumber

    for number in listNumber:
        newNumber += number

    #if newNumber not in numberCheck:
    if newNumber != 1 and newNumber != 89:
        numberCheck.append(newNumber)
        stringNumber = str(newNumber)
        #print numberCheck
    else:
        if newNumber == 1:
            finalNumberCheck = numberCheck
            finalNumberCheck.append(1)
        else:
            finalNumberCheck = numberCheck
            finalNumberCheck.append(89)

    newNumber = 0

finalNumberCheck.insert(0, inputNumber)
#print finalNumberCheck

for number in finalNumberCheck:
    if number != 1 and number != 89:
        print number, " -> ",
    else:
        print number
