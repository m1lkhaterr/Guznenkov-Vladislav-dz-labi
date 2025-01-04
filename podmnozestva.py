from itertools import product
lst = [1, 2, 3, 4]
s = list(product(lst, repeat=2))
print(s)