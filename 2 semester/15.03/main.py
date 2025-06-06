class ListMath:
    def __init__(self, s = None):
        if s is None:
            self.s = []
        else:
            self.s = []
            for i in s:
                if isinstance(i, (int, float)) and not isinstance(i, bool):
                    self.s.append(i)

    def __add__(self, other):
        return ListMath([x + other for x in self.s])

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.s = [x + other for x in self.s]
        return self

    def __sub__(self, other):
        return ListMath([x - other for x in self.s])

    def __rsub__(self, other):
        return ListMath([other - x for x in self.s])

    def __isub__(self, other):
        self.s = [x - other for x in self.s]
        return self

    def __mul__(self, other):
        return ListMath([x * other for x in self.s])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self.s = [x * other for x in self.s]
        return self

    def __truediv__(self, other):
        return ListMath([x / other for x in self.s])

    def __rtruediv__(self, other):
        return ListMath([other / x for x in self.s])

    def __itruediv__(self, other):
        self.s = [x / other for x in self.s]
        return self


lst = ListMath([1, 2.5, 3])
lst = lst + 76
print(lst.s)
lst = 6.5 + lst
print(lst.s)
lst += 76.7
print(lst.s)
lst = lst - 76
print(lst)
lst = 7.0 - lst
print(lst)
lst -= 76.3
print(lst)
lst = lst * 5
print(lst)
lst = 5 * lst
print(lst)
lst *= 5.54
print(lst)
lst = lst / 13
print(lst)
lst = 3 / lst
print(lst)
lst /= 13.0
print(lst)