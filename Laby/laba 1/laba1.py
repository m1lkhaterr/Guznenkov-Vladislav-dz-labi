def find_sum(numbers: list, target: int, index: int = 0, cur_str: str = '', cur_sum: int = 0) -> str or None:
    """
    Рекурсивная функция, которая выводит правильное равентсво через + или -.
    :param numbers: Числа для равенства
    :param target: нужное значение равенства
    :param index: порядковый номер числа, с которым работает рекурсия.
    :param cur_str: Текущее состояние равенства
    :param cur_sum: текущее значение равенства
    :return: выводит результат который равен либо строке, либо ничему (None)
    """

    if index == len(numbers): # выход из рекурсии
        if cur_sum == target:
            return cur_str # если нашлось решение
        return None # если не нашлось решение

    # рекурсия со знаком +
    str_pos = find_sum(numbers, target, index + 1, cur_str + f"+{numbers[index]}", cur_sum + numbers[index])

    if str_pos:
        return str_pos

    # рекурсия со знаком -
    str_neg = find_sum(numbers, target, index + 1, cur_str + f"-{numbers[index]}", cur_sum - numbers[index])

    if str_neg:
        return str_neg

    return None


with open("laba1.txt", "r") as f: # открываем файл и считываем с него информацию
    massive = list(map(int, f.readline().split(" ")))

n = massive[0]
numbers = massive[1:-1]
s = massive[-1]

stroka = find_sum(numbers, s) # запускаем функцию

output = '' # то что будет записываться в файл
if stroka and stroka[0] != "-":
    res = f"{stroka}={s}"
    if res[0] == "+": # если самый первый знак "+", то убираем его и записываем без него
        output = res[1:]
else:
    instance = "no solution" # если функция вывела None
with open('laba1.txt', 'a') as f: # записываем ответ в исходный файл, не удаляя из него содержимое
    f.write('\n' + output)
