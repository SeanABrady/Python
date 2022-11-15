#Ask user to enter number of digits to be calculated in Fibonacci Sequence
inputRange = int(raw_input("Please enter a number of digits to be calculated "))
#Specifying initial 2 values of fibonacci
sequence = [1, 1]
#Set initial value to 1
total = 1
#Loop from 1 to user value, shifted 1
for i in range(0, inputRange - 2):
    total += sequence[i]
    sequence.append(total)

if inputRange > 1:
    print "the first %d digits of the Fibonacci Sequence are: " % (inputRange)
    print sequence
elif inputRange == 1:
    print "the first digit of the Fibonacci Sequence is: "
    print sequence[0]
else:
    print "Invalid input"

    
    
    
    
