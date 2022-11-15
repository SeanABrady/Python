##sequence = []
##for i in range(2,101):
##    print i
##    for j in range(2,101):
##        if i ** j not in sequence:
##            sequence.append(i ** j)
##
##print len(sequence)

r = range(2, 101)

print len({a**b for a in r for b in r})
