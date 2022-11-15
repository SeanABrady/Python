userArray = []

continueCheck = True

while continueCheck == True:
    number = int(raw_input("Enter a number "))
    userArray.append(number)
    promptCheck = raw_input("Add another number? Y/N? ")
    if promptCheck == "n" or promptCheck == "N":
        continueCheck = False

runningTotal = 0

for number in userArray:
    runningTotal += number

average = runningTotal / len(userArray)

print "The average of: ",

for number in userArray:
    print number,

print "is "
print average
    
    
