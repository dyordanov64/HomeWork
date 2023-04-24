# Задача 5. За да спечели най-голямата награда в определена лотария, човек трябва да
# съпостави всичките 6 числа от билета си с 6-те числа между 1 и 49, които са изтеглени от
# организатора на лотарията. Напишете програма, която генерира произволен избор от 6
# числа за лотариен билет. Уверете се, че избраните 6 числа не се повтарят. Покажете
# числата във възходящ ред

import random

Bilet_Nombers_6_digits = []

# x = random.randint(100, size=(5))

# print(x)
# цикъл за попълване на неповтарящи се 6 числа от 0 до 9 за генерираре номер на билета
i = 0
while i < 6 :
    Bilet_Nombers_6_digits.append(random.randint(1,9))
    if Bilet_Nombers_6_digits.count(Bilet_Nombers_6_digits[i]) == 2 :
        Bilet_Nombers_6_digits.pop(i)
    else :
         i= i + 1
    # print(i)

Bilet_Nombers_6_digits.sort()

print(Bilet_Nombers_6_digits)
