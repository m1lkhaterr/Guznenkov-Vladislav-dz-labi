def lab(x, y, n, m):
    if (x, y) == (n-1, m-1):
        return 1
    if x >= n or y >= m:
        return 0
    return lab(x+1, y, n, m) + lab(x, y+1, n, m)

a, b = int(input()), int(input())
print(lab(0, 0, a, b))
print(f'{'0 ' * a}\n' * b)

