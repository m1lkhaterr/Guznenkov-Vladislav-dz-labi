res = ''
n = int(input())
rome = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
ct, b = 0, 0
k = 1000
while k != 0:
    b = n // k if n // k < 10 else (n // k) % 10
    if b:
        if b == 9:
            res += rome[ct] + rome[ct-2]
        elif 5 <= b <= 8:
            res += rome[ct-1] + (rome[ct] * (b-5))
        elif b == 4:
            res += rome[ct] + rome[ct-1]
        elif b < 4:
            res += rome[ct] * b
    ct += 2
    k //= 10
print(res)