# Реализуйте алгоритм перемешивания списка
import random


def riffle_shuffle(numbers):
    middle_index = int(len(numbers) / 2) + random.randint(0, 4)
    first_part = numbers[middle_index:]
    second_part = numbers[:middle_index]

    random_list = []
    is_first_part = True
    while len(first_part) > 0 and len(second_part) > 0:
        random_list.append(first_part.pop() if is_first_part else second_part.pop())
        is_first_part = not is_first_part

    random_list += first_part if len(first_part) > 0 else second_part

    return random_list


deck_of_cards = ["♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "♠A",
                 "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K", "♣A",
                 "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♥A",
                 "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K", "♦A"]

print(deck_of_cards)
print(riffle_shuffle(riffle_shuffle(riffle_shuffle(deck_of_cards))))
