#! python3
# StrongPassDetect - Detects if entered password is strong using regex

import re

passCharTypeRegex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$')

password = str(input("Enter your password "))

m = passCharTypeRegex.match(password)

if len(password) < 8:
    print("Your password should be at least 8 characters long")
elif m != None:
    print("Your password is strong")
else:
    print("Your password should have a mix of upper case, lower case, numeric and special characters")
