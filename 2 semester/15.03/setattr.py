class Book:
    def __init__(self, name:str = '', author:str = '', pages:int = 0, year:int = 0):
        self.name = name
        self.author = author
        self.pages = pages
        self.year = year


    def __setattr__(self, key, value):
        if key == 'author' or key == 'name':
            if isinstance(value, str):
                self.__dict__[key] = value
            else:
                raise TypeError('Неверный тип присваиваемых данных')
        elif key == 'pages' or key == 'year':
            if isinstance(value, int):
                self.__dict__[key] = value
            else:
                raise TypeError('Неверный тип присваиваемых данных')


book = Book('OOP', 'JK', 123, 2022)
print(book.name)
book1 = Book('OOP', 'JK', 123, 'yadaun')

