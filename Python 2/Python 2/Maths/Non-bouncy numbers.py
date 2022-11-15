startNumber = "10"
storeNumber = 1

while int(startNumber) < 120:
    for digit in startNumber:
        if int(digit) < storeNumber:
            startNumber = str(int(startNumber) + 1)
            storeNumber = int(digit)
        else:
            print startNumber
            startNumber = str(int(startNumber) + 1)
            storeNumber = int(digit)


            
