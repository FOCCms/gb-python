# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from decimal import Decimal

numbers = [1.1, 1.2, 3.1, 5, 10.01]

# map list filter lambda. Всё используется.
filtered_list = list(filter(lambda n: n > 0, map(lambda n: Decimal(str(n)) % 1, numbers)))
print(f"{numbers} -> {max(filtered_list) - min(filtered_list)}")
