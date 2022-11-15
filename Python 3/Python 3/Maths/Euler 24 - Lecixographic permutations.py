from itertools import permutations

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lexo = list()

lexo.append(list(permutations(numbers, 10)))

print(lexo[0][999999])





