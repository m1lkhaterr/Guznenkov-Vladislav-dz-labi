class verbose_attribute():
    # класс дескриптора
    def __get__(self, obj, type = None):
        print('accessing the attribute to get the value')
        return 42
    def __set__(self, obj, value):
        print('accessing the attributes to set the value')
        raise AttributeError('cannot change the value')

class foo():
    # экземпляр дескриптора
    attribute1 = verbose_attribute()

my_foo_object = foo()
x = my_foo_object.attribute1
print(x)