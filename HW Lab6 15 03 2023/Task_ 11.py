# # Задача 11: Да се състави програма, която извежда всички цели числа от интервала [1-
# # 50], които удовлетворяват проверка на следното условие:
# # c^3 = a^2 + b^2

# Изход:
# Found result: 2^2 + 2^2 = 2^3
# Found result: 2^2 + 11^2 = 5^3
# Found result: 5^2 + 10^2 = 5^3
# Found result: 9^2 + 46^2 = 13^3
# Found result: 10^2 + 5^2 = 5^3
# Found result: 10^2 + 30^2 = 10^3
# Found result: 11^2 + 2^2 = 5^3
# Found result: 16^2 + 16^2 = 8^3
# Found result: 18^2 + 26^2 = 10^3
# Found result: 26^2 + 18^2 = 10^3
# Found result: 26^2 + 39^2 = 13^3
# Found result: 30^2 + 10^2 = 10^3
# Found result: 39^2 + 26^2 = 13^3
# Found result: 46^2 + 9^2 = 13^3

for a in range(1,51) :
    for b in range(1,51) :
        for c in range(1,51) :
            if c ** 3 == (a ** 2) + (b ** 2) :
                print(f'{c}**3 = {a}**2 + {b}**2')
