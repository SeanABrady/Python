sequence = [1, 2]

i = 0

total = 2

while i < 4000000:
    i = sequence[len(sequence)-1] + sequence[len(sequence) - 2]
    if i < 4000000:
        sequence.append(i)
        if i % 2 == 0:
            total += i

print(sequence)
print(total)
    
