import time

t0 = time.time()

abundant = []

def find_abundant(n):
    total = 0
    numbers = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            numbers.add(i)
            numbers.add(n // i)
    if sum(numbers) - n > n:
        abundant.append(n)

for i in range(1,28124):
    find_abundant(i)

abundantSum = set()

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        abundantSum.add(abundant[i] + abundant[j])
        if (abundant[i] + abundant[j]) > 28123:
            break

nonAbundantSum = set(x for x in range(0,28124) if x not in abundantSum)

print(sum(nonAbundantSum))
t1 = time.time()

print(t1-t0, "Seconds")



        





