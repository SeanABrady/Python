continuePrompt = True
while continuePrompt == True:
    userInput = int(raw_input("Enter a number to calculate its factorial "))
    factorial = 1
    for i in range(1,userInput + 1):
        factorial *= i

    print "%d! is %d" % (userInput, factorial)

    askUser = str(raw_input("Enter another number? y/n "))
    if askUser.lower() == "n":
        continuePrompt = False
    else:
        continue
    
    
    

    
