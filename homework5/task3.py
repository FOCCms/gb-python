# 3. Создайте программу для игры в 'Крестики-нолики'.
# Реализовано на основе моего предыдущего кода, написанного на Java:
# https://github.com/FOCCms/gb-java/blob/master/src/main/java/ru/gb/lesson4/TicTacToe.java
# Можно выбрать размер поля и количество клеток подряд для победы
# Игра против ИИ. Игрок всегда ходит первым.

import random
# <DEFAULT SETTINGS>

EMPTY_CELL = ' '
CELL_X = 'X'
CELL_0 = '0'

SIZE = 3
CELLS_TO_WIN = 2
FIELD = None

AI_NAME = "Машина"
DRAW_NAME = "Дружба"
USER_NAME = "Игрок"


# </DEFAULT SETTINGS>

# <SETUP>


def setup_game():
    global USER_NAME, SIZE, CELLS_TO_WIN
    print("Привет! Прежде чем мы начнём игру ответь на несколько вопросов.")
    USER_NAME = input("Как тебя зовут: ")
    SIZE = int(input("Какой размер поля: "))
    CELLS_TO_WIN = int(input("Сколько клеток подряд нужно занять для победы: "))
    print("Отлично! Мы готовы к игре!")


def setup_field():
    return [[EMPTY_CELL] * SIZE for i in range(SIZE)]


# </SETUP>

# <SERVICES>


def get_actual_field():
    actual_field = ""
    for i in range(SIZE):
        actual_field += "----" * SIZE + "-\n"
        for j in range(SIZE):
            actual_field += f"| {FIELD[i][j]} "
        actual_field += "|\n"
    actual_field += "----" * SIZE + "-\n"
    return actual_field


def is_cell_valid(x, y):
    is_coordinate_out_of_field = x < 0 or x >= SIZE or y < 0 or y >= SIZE
    if is_coordinate_out_of_field:
        return False
    is_cell_empty = FIELD[x][y] = EMPTY_CELL
    return is_cell_empty


def make_users_turn():
    is_turn_done = False
    while not is_turn_done:
        try:
            x, y = [int(coordinate) - 1 for coordinate in input(f"Введите координаты в формате 'X Y'. "
                                                                f"Примечание: X и Y ∈ [1; {SIZE}]").split()]
            is_turn_done = is_cell_valid(x, y)
        except ValueError:
            print("Неразборчиво. Попробуйте по другому")
            pass
    FIELD[x][y] = CELL_X


def get_winner_name():
    if check_players_win(CELL_X):
        return USER_NAME
    if check_players_win(CELL_0):
        return AI_NAME
    if is_map_full():
        return DRAW_NAME
    return None


# </SERVICES>

# <WIN CHECKS>


def check_players_win(cell_char):
    """
    Для проверки необходимо пройти по массиву, размером [SIZE x SIZE], избирая на каждом шаге
    подмассив размером [CELLS_TO_WIN х CELLS_TO_WIN] и делая в нём проверку наличия ряда по вертикали,
    горизонтали или диагонали из символов cellChar(CELL_X или CELL_0) длинной CELLS_TO_WIN.

    :param cell_char: Символ, который ставит игрок или ИИ. По умолчанию X или 0.
    :return: Найден победитель ли нет
    """
    for i in range(SIZE - CELLS_TO_WIN + 1):
        for j in range(SIZE - CELLS_TO_WIN + 1):
            if check_subarray(i, j, cell_char):
                return True
    return False


def check_subarray(i, j, cell_char):
    """
    Проходим по подмассиву до тех пор пока один из счётчиков (mainDiagonal, sideDiagonal,
    verticalCount, horizontalCount) не станет равен CELLS_TO_WIN или пока не дойдём до конца подмассива.

    :param i, j: координаты смещения относительно основного массива
    :param k, l: координаты подмассива
    :param cell_char: Символ, который ставит игрок или ИИ. По умолчанию X или 0.
    """
    main_diagonal = 0
    side_diagonal = 0

    for k in range(CELLS_TO_WIN):
        # проверяем, есть ли линия по диагоналям
        if FIELD[k + i][k + j] is cell_char:
            main_diagonal += 1
        if FIELD[k + i][CELLS_TO_WIN - 1 - k - j] is cell_char:
            side_diagonal += 1

        # проверяем совпадения по вертикали и горизонтали, если их нет
        # обнуляем счётчики и переходим на следующую строку/столбец
        vertical_count = 0
        horizontal_count = 0
        for l in range(CELLS_TO_WIN):
            if FIELD[l + j][k + i] is cell_char:
                vertical_count += 1
            if FIELD[k + i][l + j] is cell_char:
                horizontal_count += 1
        # если нашли совпадение по вертикали или горизонтали -- возвращаем true
        if vertical_count == CELLS_TO_WIN or horizontal_count == CELLS_TO_WIN:
            return True
    # если нашли совпадение по одной из диагоналей -- возвращаем true
    if main_diagonal == CELLS_TO_WIN or side_diagonal == CELLS_TO_WIN:
        return True

    # если победителя нет -- возвращаем false
    return False


def is_map_full():
    for i in range(SIZE):
        for j in range(SIZE):
            if FIELD[i][j] == EMPTY_CELL:
                return False
    return True


# </WIN CHECKS>

# <AI>


def make_ai_turn():
    """
    ИИ играет по следующему принципу:
    1) методом перебора ищет поле, в которое можно поставить CELL_0 и выиграть.
        Если нашёл -- ставит, если нет -- переход к п.2
    2) методом перебора ищет поле, в которое можно поставить CELL_X и выиграть как игрок.
        Если нашёл -- ставит в него CELL_0, блокируя победу игрока, если нет -- переход к п.3
    3) генерирует координаты случайным образом до тех пор, пока не получится найти пустое поле.
        Когда находит -- ставит в него CELL_0.
    """

    # проверяем, удалось ли найти оптимальную ячейку
    is_turn_done = make_ai_predict_turn()

    # если нет -- случайный ход
    if not is_turn_done:
        make_ai_random_turn()


def make_ai_predict_turn():
    if make_predict(CELL_0):  # пытаемся победить, как ИИ
        return True
    if make_predict(CELL_X):  # пытаемся заблокировать игрока
        return True
    return False


def make_predict(predict_char):
    # идём по всему полю
    for i in range(SIZE):
        for j in range(SIZE):
            if FIELD[i][j] == EMPTY_CELL:
                # когда находим пустую ячейку, подставляем X или 0 и рассчитываем исход
                FIELD[i][j] = predict_char
                if check_players_win(predict_char):
                    # если исход успешен, занимаем данную ячейку и выходим из метода
                    FIELD[i][j] = CELL_0
                    return True
                else:
                    # иначе возвращаем пустой символ назад
                    FIELD[i][j] = EMPTY_CELL
    return False


def make_ai_random_turn():
    while True:
        x = random.randint(0, SIZE)
        y = random.randint(0, SIZE)
        if is_cell_valid(x, y):
            FIELD[x][y] = CELL_0
            break


# </AI>

# <THE GAME>

setup_game()
FIELD = setup_field()
print(get_actual_field())

winner_name = None

while True:
    # user turn
    make_users_turn()
    print(get_actual_field())

    winnerName = get_winner_name()
    if winnerName is not None:
        break

    make_ai_turn()
    print(get_actual_field())

    winnerName = get_winner_name()
    if winnerName is not None:
        break

print(f"Ура, игра окончена! И победитель это - {winnerName}!")
# </THE GAME>
