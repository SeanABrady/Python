testNumber1 = 999999
testNumber2 = 999999

palindromes = []
multiplicand1 = []
multiplicand2 = []

while testNumber1 > 99999 and testNumber2 > 99999:
    testProduct = testNumber1 * testNumber2
    display = str(testProduct)
    if display[::-1] == display:
        palindromes.append(testProduct)
        multiplicand1.append(testNumber1)
        multiplicand2.append(testNumber2)
        testNumber1 -= 1
        testNumber1 = 99999
        testNumber2 = 99999
    elif testNumber1 == 100000:
        testNumber1 = 999999
        testNumber2 -= 1
    else:
        testNumber1 -= 1
        if testNumber1 == 100000:
            testNumber1 = 999999
            testNumber2 -= 1

palindromes.sort()
index = palindromes.index(max(palindromes))
print max(palindromes)
print multiplicand1[index]
print multiplicand2[index]



