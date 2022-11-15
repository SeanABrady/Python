initValue = 2 ** 1000
#print initValue

total = 0
strValue = str(initValue)

for char in strValue:
    total += int(char)

print total
