# Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random

player1 = input("Введите имя игрока 1: ")
bot_name = "CandyBot"
player2 = input("Введите имя игрока 2 (нажмите Enter, для игры против бота): ") or bot_name
winner = None

all_candies = 150
max_candies_per_turn = 28

is_player1_turn = random.choice([True, False])
print(f"Первым ходит {player1 if is_player1_turn else player2}")


def get_input_value(player):
    while True:
        try:
            value = int(input(f"{player}, введите количество конфет (1-28): "))
            if 0 < value <= 28:
                return value
            else:
                print("Сколько?! Не-е-ет. Давай другое число")
        except ValueError:
            print("Неразборчиво. Попробуйте по другому")
            pass


def get_bot_input():
    if all_candies > max_candies_per_turn * 2:
        return random.randint(1, max_candies_per_turn + 1)  # усыпляем бдительность человеков
    else:
        return all_candies % (max_candies_per_turn + 1)  # переходим в pro режим


while winner is None:

    if is_player1_turn:
        all_candies -= get_input_value(player1)

        if all_candies <= 0:
            winner = player1
            break

        print(f"Осталось {all_candies} конфет")

    else:
        if player2 == bot_name:
            player2_turn = get_bot_input()
            print(f"{player2} забрал {player2_turn} конфет")
        else:
            player2_turn = get_input_value(player2)
        all_candies -= player2_turn

        if all_candies <= 0:
            winner = player2
            break

        print(f"Осталось {all_candies} конфет")

    is_player1_turn = not is_player1_turn

print(f"{winner} победил!")
