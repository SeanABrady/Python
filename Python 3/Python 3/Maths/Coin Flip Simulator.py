from random import randint 

coin = ["H", "T"]
headsTicker = 0
tailsTicker = 0
counter = 0
rowCount = int(input("How many coin flip results in a row do you need "))
results = []

while len(results) < 3:
    while headsTicker < rowCount and tailsTicker < rowCount:
        flip = coin[randint(0,1)]
        if flip == "H":
            headsTicker += 1
            tailsTicker = 0
            counter += 1
        if flip == "T":
            headsTicker = 0
            tailsTicker += 1
            counter += 1
    if headsTicker == rowCount:
        results.append(counter)
        headsTicker = 0
        counter = 0
    else:
        results.append(counter)
        tailsTicker = 0
        counter = 0

print(results)

averageResult = sum(results) // 3

print("It took an average of", averageResult, "flips to get", rowCount, "results in a row")
##print("The probability of getting", rowCount, "of the same result in a row is", 0.5 ** rowCount * 100, "%")    
