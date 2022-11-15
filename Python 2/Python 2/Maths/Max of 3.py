numberArray = []

while len(numberArray) < 3:
    userInput = int(raw_input("Enter a number "))
    numberArray.append(userInput)

compareInt = numberArray[0]

for number in numberArray:
    if number > compareInt:
        compareInt = number

print "The max number is %d" % (compareInt)
