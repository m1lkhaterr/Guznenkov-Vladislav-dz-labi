def santa_users(a):
    data = {}
    for i in a:
        if len(i) > 1:
            data[i[0]] = i[1]
        else:
            data[i[0]] = None
    return data

x = [['name1 surname1', 12345], ['name2 surname2'], ['name3 surname3', 12354], ['name4 surname4', 12435]]
print(santa_users(x))