s = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]
d = {}
for i in s:
    k = (''.join(sorted(i)), len(i))
    if k not in d.keys():
        d[k] = []
    d[k].append(i)
print(list(d.values()))