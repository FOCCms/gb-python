# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


def negative_fibonacci_of(fibonacci):
    fibonacci[2::2] = [x * -1 for x in fibonacci[2::2]]
    return list(reversed(fibonacci))


k = int(input("Введите число: "))
fibonacci_list = [fibonacci_of(n) for n in range(k + 1)]
negative_fibonacci_list = negative_fibonacci_of(fibonacci_list.copy())

print(f"для k = {k} список будет выглядеть так: {negative_fibonacci_list + fibonacci_list[1:]}")
