from abc import abstractmethod

class Box:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def count(self):
        pass

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class DictBox(Box):
    def __init__(self, items = None):
        if items is None:
            self.items = {}
        else:
            self.items = items

    def add(self, items):
        for item in items:
            if item.name not in self.items:
                self.items[item.name] = [item.value]
            else:
                self.items[item.name] += [item.value]

    def empty(self):
        temp = [x[y] for x in self.items.values() for y in range(len(x))]
        self.items = {}
        return temp


    def count(self):
        return len(self.empty())

    def get_items(self):
        items = [Item(key, val) for key in self.items for val in self.items[key]]
        return items

    def get_values(self):
        return [x[y] for x in self.items.values() for y in range(len(x))]

class ListBox(Box):
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def add(self, items):
        for item in items:
            self.items.append(item)

    def empty(self):
        temp = [item.value for item in self.items]
        self.items = []
        return temp

    def count(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def get_values(self):
        return [item.value for item in self.items]


def repack_boxes(*args):
    ov_its = []
    for box in args:
        temp = box.get_items()
        ov_its += temp
        box.empty()
    c = len(ov_its)//len(args)
    for box in args:
        box.add(ov_its[:c])
        ov_its = ov_its[c:]
    if ov_its:
        args[-1].add(ov_its)
    return

b1 = DictBox()
b2 = ListBox()
b3 = DictBox()
b1.add([Item('h', 1), Item('uy', 2), Item('uy', 5)])
b2.add([Item('ttt', 3), Item('te', 2), Item('ffffff', 9), Item('re', 3), Item('eaaa', 6)])
b3.add([Item('xd', 999), Item('xd', 69)])
print(b1.get_values(), b2.get_values(), b3.get_values())
# print(b1.empty(), b2.empty())
repack_boxes(b1, b2, b3)
print(b1.get_values(), b2.get_values(), b3.get_values())

