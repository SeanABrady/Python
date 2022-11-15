sums = set()

for i in range(1,295246): #2952469**5 *5
    a = str(i)
    b = [i for i in a]
    total = 0
    for number in b:
        total += int(number)**5
    if total == i and total != 1:
        sums.add(i)

print(sum(sums))
           
        
    
