# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from itertools import product


def check_predicate(x, y, z):
    return not (x or y or z) == (not x and not y and not z)


for value in [seq for seq in product((True, False), repeat=3)]:
    print(f"x = {value[0]}, y = {value[1]}, z = {value[2]} -> {check_predicate(value[0], value[1], value[2])}")

# x = True, y = True, z = True -> True
# x = True, y = True, z = False -> True
# x = True, y = False, z = True -> True
# x = True, y = False, z = False -> True
# x = False, y = True, z = True -> True
# x = False, y = True, z = False -> True
# x = False, y = False, z = True -> True
# x = False, y = False, z = False -> True
