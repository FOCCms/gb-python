# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = abs(int(input("Введите число: ")))

sequence = list(range(-n, n + 1))
indexes = []
prod = 1
with open("file.txt", "r") as file:
    for line in file:
        i = int(line.strip())
        prod *= sequence[i]
        indexes.append(i)

print(f"N = {n}, sequence = {sequence}, indexes = {indexes}, product = {prod}")
# N = 10, sequence = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], indexes = [0, 2, 4, 7], product = 1440
