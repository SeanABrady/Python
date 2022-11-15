numbers = []
#Allow user to enter any number of numbers, and stops when they enter 'n'
decision = False
while decision == False:
    check = raw_input("Please enter a number (blank to quit) ")
    if check != "":
        numbers.append(int(check))
    else:
        decision = True

#Store initial values for calculating LCM later on
placeholder1 = numbers[0]
placeholder2 = numbers[1]

#Find the LCM for the first 2 numbers in the list
while placeholder1 != 0 and placeholder2 != 0:
    if placeholder1 > placeholder2:
        placeholder1 = placeholder1 % placeholder2
        if placeholder1 == 0:
            lcm = (numbers[0] * numbers[1])/placeholder2
            break
    if placeholder2 > placeholder1:
        placeholder2 = placeholder2 % placeholder1
        if placeholder2 == 0:
            lcm = (numbers[0] * numbers[1])/placeholder1
            break

#for subsequent numbers in list, calculate LCM between new number and previous LCM
for i in range (2, len(numbers)):
    placeholder = numbers[i]
    lcm2 = lcm
    while placeholder != 0 and lcm != 0:
        if placeholder > lcm and lcm != 0:
            placeholder %= lcm
            if placeholder == 0:
                lcm = (lcm2 * numbers[i])/lcm
                break
        if lcm > placeholder and placeholder != 0:
            lcm = lcm % placeholder
            if lcm == 0:
                lcm = (lcm2 * numbers[i])/placeholder
                break

print "The least common multiple of",
for number in numbers:
    print  "%d," % (number),
print "is:"
print lcm
