class Factory:
    @staticmethod
    def build_sequence():
        a = list()
        return a

    @staticmethod
    def build_number(string):
        string = int(string)
        return string

class Loader:
    @staticmethod
    def parse_format(string, factory):
        a = factory.build_sequence()
        for i in string.split(','):
            c = factory.build_number(i)
            a.append(c)
        return a

loader = Loader
print(loader.parse_format('4, 5, -6', Factory))
