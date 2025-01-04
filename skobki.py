def skobki(s, n):
    if s.count('(') > n or s.count(')') > n:
        return
    if len(s) == 2 * n:
        if s[-1] == '(':
            return
        print(s)
        return
    return skobki(s+'(', n), skobki(s+')', n)

n = int(input())
skobki('(', n)
