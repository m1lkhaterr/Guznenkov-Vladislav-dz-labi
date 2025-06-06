from string import digits, ascii_lowercase


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return '\n'.join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    chars = "йцукенгшщзхъфывапролджэячсмитьбю" + ascii_lowercase
    chars_correct = chars + chars.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class='login'><{self.name}>: <input type='text' size=<{self.size}> />"

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("Некорректное поле name")
        for i in name:
            if i not in cls.chars_correct:
                raise ValueError("Некорректное поле name")


class PasswordInput:
    chars = "йцукенгшщзхъфывапролджэячсмитьбю" + ascii_lowercase
    chars_correct = chars + chars.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class='password'><{self.name}>: <input type='text' size=<{self.size}> />"

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("Некорректное поле name")
        for i in name:
            if i not in cls.chars_correct:
                raise ValueError("Некорректное поле name")


login = FormLogin(TextInput('Логин'), PasswordInput('Пароль'))
html = login.render_template()
print(html)