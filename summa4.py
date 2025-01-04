n = int(input())
s = []
res = []
for _ in range(n):
    s.append(int(input()))
f = int(input())
mc = abs(f) + 999999999
for a in range(len(s) - 3):
    for b in range(a+1, len(s) - 2):
        for c in range(b+1, len(s) - 1):
            for d in range(c+1, len(s)):
                cur = [s[a], s[b], s[c], s[d]]
                summ = sum(cur)
                if abs(summ-f) < abs(mc-f):
                    mc = summ
                    res = cur
print(res, mc)
