# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


def prod_list(numbers):
    prod = []
    while len(numbers) > 0:
        first_element = numbers.pop(0)
        if len(numbers) > 0:
            prod.append(first_element * numbers.pop())
        else:
            prod.append(first_element * first_element)
    return prod


l1 = [2, 3, 4, 5, 6]
l2 = [2, 3, 5, 6]

print(f"{l1} -> {prod_list(l1.copy())}")
print(f"{l2} -> {prod_list(l2.copy())}")
