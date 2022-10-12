# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

input_value = int(input("Введите число: "))
n = input_value
i = 2
prod_factors = []
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        prod_factors.append(i)
if n > 1:
    prod_factors.append(n)

print(f"N = {input_value} -> {prod_factors}")
