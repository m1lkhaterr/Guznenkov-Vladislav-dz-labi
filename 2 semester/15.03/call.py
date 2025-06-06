from random import randint, choice

class RandomPassword:
    def __init__(self, psw_chars, max_length, min_length):
        self.psw_chars = psw_chars
        self.max_length = max_length
        self.min_length = min_length

    def __call__(self):
        length = randint(self.min_length, self.max_length)
        password = ''.join(choice(self.psw_chars) for _ in range(length))
        return password

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 20, 5)
lst_pass = [rnd(), rnd(), rnd()]
print(lst_pass)