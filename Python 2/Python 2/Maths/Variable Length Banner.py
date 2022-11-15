userTitle = str(raw_input("Enter a title "))

counter = 0

for char in userTitle:
    counter += 1

print "*" * (counter + 4)
print "* %s *" % userTitle
print "*" * (counter + 4)
