text = "Python!"
revInt = []
revInt.extend(text)
counter = int(len(revInt) - 1)
print counter
print revInt
reverse = []
while counter >= 0:
    reverse.append(revInt[counter])
    counter += -1

reverse = str(reverse)
print reverse
