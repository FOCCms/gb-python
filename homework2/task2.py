# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math

n = int(input("Введите число: "))

result = {1: "1"}

for i in range(2, n+1):
    sequence = list(range(1, i + 1))
    result[math.prod(sequence)] = "*".join(map(str, sequence))

print(f"Пусть N = {n}, тогда [{', '.join(map(str, result.keys()))}] ({', '.join(result.values())})")
