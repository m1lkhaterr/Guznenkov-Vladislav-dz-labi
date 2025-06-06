class NewList:
    def __init__(self, lst):
        self.lst = lst

    def __sub__(self, other):
        dict1 = {}
        for i in other.lst:
            if (i, type(i)) in dict1:
                dict1[(i, type(i))] += 1
            else:
                dict1.setdefault((i, type(i)), 1)
        new_lst = []
        for i in self.lst:
            pair = (i, type(i))
            if pair in dict1 and dict1[pair] > 0:
                dict1[(i, type(i))] -= 1
            else:
                new_lst.append(i)
        return NewList(new_lst)

    def __rsub__(self, other):
        return self-other

    def get_list(self):
        return self.lst

test1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
test2 = NewList([0, 1, 2, 3, True])
test3 = test1-test2
test1 -= test2
print(test1.get_list())
print(test3.get_list())

test10 = NewList([95, 3, 3, 95, 2, 95])
test20 = NewList([95, 3])
test30 = test10-test20
print(test30.get_list())