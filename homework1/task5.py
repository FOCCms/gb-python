# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

Ax = int(input("Введите координату Ax: "))
Ay = int(input("Введите координату Ay: "))

Bx = int(input("Введите координату Bx: "))
By = int(input("Введите координату By: "))

distance = math.sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)

print(f"A ({Ax}.{Ay}); B ({Bx},{By}) -> {distance:.2f}")