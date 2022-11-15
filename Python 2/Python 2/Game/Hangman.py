inputWord = raw_input("Enter a word ")
guessWord = []

for letter in inputWord:
    guessWord.append("#")

print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print
print

wordList = []
for char in inputWord:
    wordList.append(char)
    print "_ ",

found = False
guessCounter = 0

while guessCounter <= 6:
    guessLetter = raw_input("Guess a letter ")
    storePosition = []

    counter = 0
    for letter in wordList:
        if guessLetter == letter:
            storePosition.append(counter)
            counter += 1
            found = True
        else:
            counter += 1

    if found == False:
        guessCounter += 1
    else:
        found = False
        
    for i in range(0,len(storePosition)):
        guessWord[storePosition[i]] = guessLetter

    print guessWord

