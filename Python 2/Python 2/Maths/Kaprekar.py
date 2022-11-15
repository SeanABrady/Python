userInputMin = int(input("Please enter a number to start the range "))
userInputMax = int(input("Please enter a number to end the range "))

from datetime import datetime
startTime = datetime.now()

outputNumbers = []

k = userInputMin
while k < userInputMax:
    calcSquare = k ** 2
    stringSquare = str(calcSquare)
    isKaprekar = False

    i = 1
    while i < len(stringSquare):
        test1 = int(stringSquare[0:i])
        test2 = int(stringSquare[i:(len(stringSquare))])
        if test1 + test2 == k and test1 != 0 and test2 != 0:
            isKaprekar = True
        i += 1

    if isKaprekar == True:
        print "%d is a Kaprekar number!" % (k)
        #print "%d ^ 2 = %d, %d + %d = %d" (k, calcSquare, test1, test2, k)
        outputNumbers.append(k)

    k += 1
print ""   
print "It took me this long to calculate:",
print datetime.now() - startTime
