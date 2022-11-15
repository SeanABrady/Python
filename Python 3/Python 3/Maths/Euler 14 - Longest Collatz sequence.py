counter = 0
maxSequence = 0

for i in range(1000000, 1, -1):
    numberCheck = i
    while numberCheck != 1:
        if numberCheck % 2 == 0:
            counter += 1
            numberCheck /= 2
        elif numberCheck % 2 != 0 and numberCheck != 1:
            counter += 1
            numberCheck = numberCheck * 3 + 1
    if counter > maxSequence:
        maxSequence = counter
        maxNumber = i
        counter = 0
    else:
        counter = 0

print(maxNumber)
print(maxSequence)
