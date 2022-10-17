# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

def single_elements_counter(n: str):
    return [i for i in range(10) if n.count(str(i)) == 1]


print(f"47756688399943 -> {single_elements_counter(str(47756688399943))}")
print(f"1113384455229 -> {single_elements_counter(str(1113384455229))}")
print(f"1115566773322 -> {single_elements_counter(str(1115566773322))}")
