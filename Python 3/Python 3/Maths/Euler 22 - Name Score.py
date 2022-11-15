wordArray = []
total = 0

with open("namesSorted.txt", "w") as namesFileSorted:
    with open("names.txt", "r") as namesFile:
        for line in namesFile:
            currentLine = line.split(",")
        for word in currentLine:
            wordArray.append(word)
        wordArray.sort()
        for name in wordArray:
            namesFileSorted.write("%s\n" % name)

    for name in wordArray:
        wordTotal = 0
        namePosition = wordArray.index(name) + 1
        low = name.lower()
        low = low[1:len(low) - 1]
        for char in low:
            wordTotal += (ord(char) - 96)
        wordTotal *= namePosition
        total += wordTotal

print(total)

        

    

        

        
        
