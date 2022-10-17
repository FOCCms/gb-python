# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input("Введите количество чисел последовательности: "))

# sequence = []
# for i in range(1, n+1):
#     sequence.append(pow(1+1/i, i))

print(f"{n} -> {sum([pow(1+1/i, i) for i in range(1, n+1)])}")
