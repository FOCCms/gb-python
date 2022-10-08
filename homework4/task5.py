# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0
import re

small_numbers_mapper = {'⁰': 0, '¹': 1, '²': 2, '³': 3, '⁴': 4, '⁵': 5, '⁶': 6, '⁷': 7, '⁸': 8, '⁹': 9}


def parse_polynomial(polynomial):
    polynomial_dict = {}
    print(polynomial)
    polynomial = polynomial.split("=")[0]
    for item in re.findall("[-+]?\\s?\\d*x?[⁰¹²³⁴⁵⁶⁷⁸⁹]*\\s", polynomial):
        try:
            value, key = str(item).replace(" ", "").split("x")
        except ValueError:
            value, key = str(item).replace(" ", "").split("x")[0], "⁰"  # парсит последнее число без x и степени
        try:
            value = int(value)
        except ValueError:
            value = 1 if value == "+" else -1  # если перед x нет числа
        polynomial_dict[small_numbers_mapper[key]] = value
    return polynomial_dict


def dict_to_polynomial(polynomial_dict: dict):
    polynomial = ""
    for item in polynomial_dict:
        number = polynomial_dict[item]
        i = item
        if number == 0:
            continue
        if len(polynomial) == 0:
            polynomial += f"{number}x^{list(small_numbers_mapper.keys())[list(small_numbers_mapper.values()).index(item)]} "  # добавляет первое число без знака +, но со знаком минус
        elif i == 0:
            polynomial += f"{'{0:+}'.format(number)} "  # добавляет последнее число без x и степени
        elif i == 1:
            polynomial += f"{'{0:+}'.format(number)}x "  # добавляет предпоследнее число без значения степени
        else:
            polynomial += f"{'{0:+}'.format(number)}x^{list(small_numbers_mapper.keys())[list(small_numbers_mapper.values()).index(item)]} "

    polynomial = polynomial.replace("(\\D)1x", "x")
    polynomial += "= 0"
    return polynomial


dict1 = {}
dict2 = {}

with open("input1.txt", "r") as file:
    dict1 = parse_polynomial(file.readline())

with open("input2.txt", "r") as file:
    dict2 = parse_polynomial(file.readline())
result = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
sorted_result = dict(reversed(sorted(result.items())))

with open("result.txt", "w") as file:
    file.write(f"{dict_to_polynomial(sorted_result)}")
