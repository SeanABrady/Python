from itertools import islice

digits = []

def infinite_divide(numerator,denominator):
    if numerator > denominator:
        raise ValueError('This function only returns digits after the decimal')
    while numerator != 0:
        numerator *= 10
        digit, numerator = divmod(numerator, denominator)
        yield digit

for i in range(1, 1000):
    digits.append(''.join(str(digit) for digit in islice(infinite_divide(1,i),2000)))

noTests = len(digits)
maxDecimals = [0,0]

for c in range(0,noTests):
    lengthDecimal = len(digits[c])
    b = lengthDecimal - 2
    match = False
    while b >= (lengthDecimal / 2) and match == False:
        a = digits[c][lengthDecimal:b:-1]
        if a == (digits[c][b:(b-len(a)):-1]):
            match = True
            if len(a) > maxDecimals[0]:
                maxDecimals = [len(a), c + 1]
        b -= 1

print(maxDecimals)


