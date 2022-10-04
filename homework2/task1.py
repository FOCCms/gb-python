# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = abs(float(input("Введите дробное число: ")))

fractional_part_size = len(str(n).split(".")[1])

n *= 10 ** fractional_part_size

summa = 0
while n != 0:
    summa += int(n % 10)
    n //= 10

print(summa)
