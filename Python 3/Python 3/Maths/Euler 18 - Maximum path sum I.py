numberArray = []
tempArray = []
rowArray = []
i = 0

with open("pyramidII.txt", "r") as pyramid:
    for number in pyramid:
        numberString = number
        
numberArray = numberString.split(' ')

print(len(numberArray))

for j in range(0, len(numberArray)):
    tempArray.append(int(numberArray[j]))
    if len(tempArray) >= i + 1:
        rowArray.append(tempArray)
        tempArray = []
        i += 1

finalRow = []

for i in range(len(rowArray) - 2, -1, -1):    
    firstRow = rowArray[i + 1]
    secondRow = rowArray[i]
    for i in range(0, len(secondRow)):
        if secondRow[i] + firstRow[i] > secondRow[i] + firstRow[i + 1]:
            finalRow.append(secondRow[i] + firstRow[i])
        else:
            finalRow.append(secondRow[i] + firstRow[i + 1])
    rowArray[i] = finalRow
    finalRow = []

print(rowArray[0])





        

