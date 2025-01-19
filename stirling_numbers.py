import sys

sys.setrecursionlimit(2000)
def stir_nums(a,b):
    if a < b or b == 0:
        return 0
    if a == b:
        return 1
    if a > b > 0:
        return stir_nums(a-1,b-1) + b*stir_nums(a-1,b)

a, b = int(input()), int(input())
print(stir_nums(a, b))

