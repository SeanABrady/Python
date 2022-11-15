a = 0
b = 0
c = 0

for a in range(100,751):
    for b in range(100, 751):
        for c in range(100, 751):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print("%d^2 x %d^2 = %d^2" % (a, b, c))
                break
            else:
                continue

            
