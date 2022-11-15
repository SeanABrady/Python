numberCheck = int(raw_input("Enter a number to check if it's prime! "))

from datetime import datetime
startTime = datetime.now()

while numberCheck < 4:
    if numberCheck == 1:
        print "1 is not a prime number! Its factor is 1!"
        numberCheck = int(raw_input("Enter another number!"))
    if numberCheck == 2:
        print "2 is a prime number! Its factors are 1 and 2!"
        numberCheck = int(raw_input("Enter another number!"))
    if numberCheck == 3:
        print "3 is a prime number! Its factors are 1 and 3!"
        numberCheck = int(raw_input("Enter another number!"))

counter = 2
counterTwo = 2
prime = False
factors = [1, numberCheck]

while counter <= int(numberCheck/2):
    if numberCheck % counter != 0:
        prime = True
        counter += 1
    else:
        prime = False
        counter += 1
        print ""
        print "This number is not a prime, calculating factors..."
        print ""
        break

if prime == True:
    print "%d is a prime number! Its factors are %d and %d" % (numberCheck,1,numberCheck)
else:
    while counterTwo <= numberCheck/2:
        factorCheck = numberCheck % counterTwo
        counterTwo += 1
        if factorCheck % counterTwo == 0:
            print "I have found a factor: %d" % (counterTwo - 1)
            factors.append(counterTwo - 1)

    print ""
    print "%d is not a prime number!" % (numberCheck)
    print "Its factors are:"
    factors.sort()
    print factors
    
print ""   
print "It took me this long to calculate:",
print datetime.now() - startTime
