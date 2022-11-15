inputNumber = raw_input("Enter a number ")

forward = str(inputNumber)
reverse = forward[::-1]
counter = 0

while forward != reverse:
    #print forward, "+", reverse, "=",
    forward = str(int(forward) + int(reverse))
    reverse = forward[::-1]
    counter += 1
    #print forward
    if counter == 50000:
        print "No palindrome found after 50000 iterations"
        print "Resulting number has", len(forward), "digits"
        print forward
        break

if counter == 1:
    print "This took 1 iteration"
else:
    print "This took", counter, "iterations"
