def mark_moves(board: list, pos: tuple, n: int):
    """
    Функция, помечающая все возможные ходы фигуры на доске
    :param board: доска
    :param pos: позиция фигуры
    :param n: размер доски (n**2)
    :return: не нужен тут
    """
    horse_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)] # ходы конем
    for fx in range(n): # помечаем ходы ферзем
        board[fx][pos[1]] = '*'
        board[pos[0]][fx] = '*'
        if pos[0] - fx >= 0 and pos[1] - fx >= 0:
            board[pos[0] - fx][pos[1] - fx] = '*'
        if pos[0] + fx < n and pos[1] + fx < n:
            board[pos[0] + fx][pos[1] + fx] = '*'
        if pos[0] - fx >= 0 and pos[1] + fx < n:
            board[pos[0] - fx][pos[1] + fx] = '*'
        if pos[0] + fx < n and pos[1] - fx >= 0:
            board[pos[0] + fx][pos[1] - fx] = '*'
        for dx, dy in horse_moves: # помечаем ходы конем
            if 0 <= pos[0] + dx < n and 0 <= pos[1] + dy < n:
                board[pos[0] + dx][pos[1] + dy] = '*'
        board[pos[0]][pos[1]] = '#' # ставим саму фигуру



def unmark_moves(board: list, pos: tuple, n: int):
    """
    Функция, возвращающая доску в состояние до размещения новой фигуры
    :param board: доска
    :param pos: позиция фигуры, ходы которой нужно убрать (и её саму)
    :param n: размер доски (n**2)
    :return: не нужен тут
    """
    board[pos[0]][pos[1]] = '0' # убираем фигуру с доски
    for x in range(n): # убираем все возможные ходы фигур
        for y in range(n):
            if board[x][y] == '*':
                board[x][y] = '0'
    for x in range(n): # помечаем все возможные ходы расставленных фигур на доске заново, но уже без убранной фигуры
        for y in range(n):
            if board[x][y] == '#':
                mark_moves(board, (x, y), n)


def place_figure(board: list, l: int, n: int, positions: list, start_x: int, start_y: int, placed_figures: list) -> None:
    """
    Рекурсивная функция, расстанавливающая фигуры на доске
    :param board: доска
    :param l: количество оставшихся фигур для расстановки
    :param n: размер доски (n**2)
    :param positions: список с координатами расставленных фигур (в последствии выполнения функции)
    :param start_x: переменная, используемая в цикле перебора координат, чтобы при каждом новом входе в рекурсию отсчет
    координат не начинался с нуля
    :param start_y: тоже самое, что и start_x, но при втором и последующих циклах row изменяется на 0 (чтобы было как
    (8,9), (9, 0), (9,1)..., а не (8,9), (9,9))
    :param placed_figures: уже поставленные на доску из условия фигуры
    :return: выход из рекурсии чтобы комп не лопнул
    """
    global a
    if l == 0: # все фигуры расставлены, выход из рекурсии
        a = True
        out.write(f'{placed_figures + positions}\n')
        return

    for row in range(start_x, n): # цикл, перебирающий все возможные координаты на доске
        for col in range(start_y if row == start_x else 0, n):
            if board[row][col] == '0': #  проверка не под боем ли клетка
                positions.append((row, col))  # добавляем координаты новой фигуры
                mark_moves(board, (row, col), n) # помещаем фигуру на доску

                place_figure(board, l - 1, n, positions, row, col, placed_figures) # рекурсия

                unmark_moves(board, (row, col), n) # откатываем изменения
                positions.pop()
    return


f = open('input.txt', 'r') # открываем файл с входными данными и считываем с него информацию
nlk = list(map(int, f.readline().split()))
n, l, k = nlk[:3]
init_pos = []
for _ in range(k):
    x, y = map(int, f.readline().split())
    init_pos.append((x, y))
a = False # переменная, показывающая, что функция нашла хотя бы 1 решение


board = [['0' for _ in range(n)] for _ in range(n)] # инициализация доски
for pos in init_pos:
    mark_moves(board, pos, n)
print(''.join([''.join(x) + '\n' for x in board])) # вывод исходной доски (по приколу)

out = open('output.txt', 'w') # открываем файл вывода
place_figure(board, l, n, [], 0, 0, init_pos) # входим в функцию, расставляющую фигуры
if not a:
    out.write('no solutions')
f.close() # закрываем файлы
out.close()