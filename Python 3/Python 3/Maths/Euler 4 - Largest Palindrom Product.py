results = []

for i in range(999,900, -1):
    for j in range(999,900, -1):
        if str(i * j) == (str(i * j))[::-1]:
            results.append(i*j)


print(max(results))

            
