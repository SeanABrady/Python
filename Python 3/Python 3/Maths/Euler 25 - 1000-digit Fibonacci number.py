n1 = 1
n2 = 2
placeholder = 0
i = 3

while len(str(n2)) < 1000:
   placeholder = n2
   n2 = n2 + n1
   n1 = placeholder
   i += 1

print(n2, i)
