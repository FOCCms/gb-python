# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k.
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
import random

k = int(input("Введите число: "))

polynomial = ""

for i in range(k, -1, -1):
    number = random.randint(-100, 100)
    if number == 0:
        continue
    if len(polynomial) == 0:
        polynomial += f"{number}x^{i} "  # добавляет первое число без знака +, но со знаком минус
    elif i == 0:
        polynomial += f"{'{0:+}'.format(number)} "  # добавляет последнее число без x и степени
    elif i == 1:
        polynomial += f"{'{0:+}'.format(number)}x "  # добавляет предпоследнее число без значения степени
    else:
        polynomial += f"{'{0:+}'.format(number)}x^{i} "

polynomial += "= 0"

with open("output.txt", "w") as file:
    file.write(f"k={k} -> {polynomial}")
