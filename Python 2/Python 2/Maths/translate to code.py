userString = raw_input("Enter a sentence to encode ")
userString = userString.lower()
encodedList = []

for char in userString:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        encodedList.append(char)
    elif char == " ":
        encodedList.append(char)
    else:
        encodedList.append(char)
        encodedList.append("o")
        encodedList.append(char)

codeword = "".join(encodedList)

print codeword
        
