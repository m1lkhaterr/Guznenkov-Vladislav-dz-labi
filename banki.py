num, lst = 7, [('sber', 10), ('tin', 5), ('vol', 6), ('ker', 12), ('bkb', 23), ('lina', 3), ('huy', 59)]# rip tinker
lst.append(lst[-1])
new = [0] + [x[1] for x in lst] if num > 2 else [x[1] for x in lst]
k = 0
banks = []
if num > 2:
    for ind in range(len(new) - 3):
        trp = [new[ind + g] for g in range(3)]
        mx = new[ind + 2] = max(trp[1], trp[0] + trp[2])
        if mx == trp[1]:
            banks.append((lst[ind][0], ind + 1))
            # if (lst[ind][0], ind + 1) not in banks:
            #     banks.append((lst[ind][0], ind + 1))
            # k = 0
        else:
            k += 1
            if k == 1:
                if ind == 0:
                    banks.append((lst[2][0], 2))
                elif len(banks) == 1:
                    banks.append((lst[ind+1][0], ind+2))
                else:
                    banks += [(lst[ind + 1][0], ind + 2)]
            elif k == 2:
                banks = banks[:-1] + [(lst[ind + 1][0], ind + 2)]
            else:
                banks = banks[:-1] + [(lst[ind - 1][0], ind), (lst[ind + 1][0], ind + 2)]
                k = 0
        print(ind)
        print(new)
        print(banks)
elif num == 2:
    mx = max(new[1], new[0] + new[2])
    if mx == new[1]:
        banks.append(lst[1])
    else:
        banks = banks[:-1]
        banks.extend((lst[0], lst[2]))
else:
    banks.append(lst[0])
print(new[-2] if num > 2 else new[-1], banks, sep='\n')
