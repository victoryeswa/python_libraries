#itertools: product, permutations, accumilate, groupby, and infinite iterators

from itertools import product

a = [1, 2]

b = [3, 4]

prod = product(a, b)

print(list(prod))

#we can define the number of repetitions

a = [1, 2]
b = [3]
prod1 = product (a, b, repeat=2)

print(list(prod1))

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)

print(list(perm))