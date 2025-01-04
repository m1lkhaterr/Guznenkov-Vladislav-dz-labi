list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
a = list(filter(lambda x: x in list1, list2))
b = list(filter(lambda x: x not in a, list1+list2))
c = list(filter(lambda x: x not in a, list1))
d = list(filter(lambda x: x not in a, list2))
print(f"1) {len(a)}: {a}")
print(f"2) {len(b)}: {b}")
print(f"3) {len(c)}: {c}")
print(f"4) {len(d)}: {d}")
