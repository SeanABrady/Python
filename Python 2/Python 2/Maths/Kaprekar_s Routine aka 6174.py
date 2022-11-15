acceptable = False
while acceptable == False:
    inputNumber = int(raw_input("Enter a 4 digit number, and watch it become 6174! "))
    if inputNumber > 999 and inputNumber < 9999 and inputNumber % 1111 != 0:
        acceptable = True
    if inputNumber % 1111 == 0:
        print "The 4-digit number can't be a multiple of 1111. "
    else:
        continue

resInt = inputNumber

while resInt != 6174:
    strInt = str(resInt)
    listInt = []

    for digit in strInt:
        listInt.append(int(digit))

    ascList = sorted(listInt, key=int)
    descList = sorted(listInt, key=int, reverse=True)

    def magic(numList):         
        s = map(str, numList)   
        s = ''.join(s)          
        s = int(s)              
        return s

    ascInt = magic(ascList)
    descInt = magic(descList)
    resInt = descInt - ascInt

    print "%d - %d =" % (descInt,ascInt),
    print resInt



    





