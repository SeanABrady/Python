userInput = int(raw_input("Enter a number to check if it's a factorial "))
factorial = []
i = 1
numberCheck = userInput / i
while i < userInput:
    if numberCheck % i == 0:
        numberCheck = numberCheck / i
        factorial.append(i)
        i += 1
        if numberCheck == 1:
            i += userInput
    else:
        i += 1

if len(factorial) != factorial[len(factorial) - 1]:
    print "%d is not a factorial." % userInput
else:
    print userInput, "is %d!" % (factorial[len(factorial) - 1])
