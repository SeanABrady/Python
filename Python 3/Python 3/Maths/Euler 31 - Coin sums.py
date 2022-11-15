def change(total, denominations):
    r = [1] + [0] * 200
    for k in denominations:
        for i in range(k, len(r)):
            r[i] += r[i - k]
    return r[total]

print(change(200, (200,100,50,20,10,5,2,1)))
