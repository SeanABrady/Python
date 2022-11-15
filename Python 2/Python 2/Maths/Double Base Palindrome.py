startValue = int(raw_input("Enter a number in base 10 to start the range "))
endValue = int(raw_input("Enter a number in base 10 to end the range "))

for i in range(startValue,endValue + 1):
    strCheck = str(i)
    if strCheck[::-1] == strCheck:
        maxCheck = 0
        calcNumber = i
        while 2 ** maxCheck < calcNumber:
            maxCheck += 1
        productList = []
        counter = 0
        while maxCheck >= 0:
            if calcNumber - 2 ** maxCheck >= 0:
                calcNumber -= 2 ** maxCheck
                counter += 1
            else:
                productList.append(counter)
                counter = 0
                maxCheck -= 1

        if productList[0] == 0:
            productList.remove(0)

        compare = "".join(map(str, productList))
        compareInit = str(i)

        if compare[::-1] == compare and compareInit[::-1] == compareInit:
            print compareInit, compare

