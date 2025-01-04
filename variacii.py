from itertools import permutations
s = [1,2,3]
a = list(map(list, (permutations(s, r=len(s)))))
print(a)