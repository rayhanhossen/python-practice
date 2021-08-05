from itertools import product, permutations, combinations, accumulate, groupby, combinations_with_replacement, cycle, \
    repeat

print('------Working with product-------')

a = [1, 2]
b = [3, 4]

prod = product(a, b, repeat=2)
print(list(prod))

print('------Working with permutations-------')

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

print('--------Working with combinations-------')

a = [1, 2, 3, 4]

comb = combinations(a, 2)
print(list(comb))

comb_re = combinations_with_replacement(a, 2)
print(list(comb_re))

print('--------Working with accumulate-------')
a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))

print('--------Working with groupby-------')

a = [1, 2, 3, 4]

group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

print('--------Working with cycle-------')

a = [1, 2, 3]

for i in cycle(a):
    print(i)

print('--------Working with repeat-------')

for i in repeat(1, 4):
    print(i)
