#Ask user for number and base conversion
inputNumber = int(raw_input("Enter a number in base 10 "))
inputBase = int(raw_input("Enter a base to convert it to "))

calcNumber = inputNumber

#Finds largest index of base which fits into inputNumber
maxCheck = 0
while inputBase ** maxCheck  < inputNumber:
    maxCheck += 1

#Have to clone above to add trailing 0s later on
trailingZeroes = maxCheck

#Define empty list
productList = []
#Initial value for counter
counter = 0
#Since 1 is the lowest value we care about, the index only needs to go to 0
while maxCheck >= 0:
    #Take away the highest exponent possible that still leaves a value greater than 0
    if calcNumber - inputBase ** maxCheck >= 0:
        calcNumber = calcNumber - inputBase ** maxCheck
        counter += 1
    #If this exponent can't be taken out again
    else:
        #add the counter to productList
        productList.append(counter)
        #reset counter
        counter = 0
        #decrease index
        maxCheck = maxCheck - 1

#If the list is shorter than the largest index, add 0s until it's the same length
while len(productList) <= trailingZeroes:
    productList.append(0)

if productList[0] == 0:
    productList.remove(0)

for i in range(0,len(productList)):
    if productList[i] == 10:
        productList[i] = "A"
    if productList[i] == 11:
        productList[i] = "B"
    if productList[i] == 12:
        productList[i] = "C"
    if productList[i] == 13:
        productList[i] = "D"
    if productList[i] == 14:
        productList[i] = "E"
    if productList[i] == 15:
        productList[i] = "F"

#Convert the list into a string then print it
print "".join(map(str, productList))

 
    
