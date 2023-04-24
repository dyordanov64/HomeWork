# Задача 5. Да се напише програма, която да намира броят на четните и нечетните числа
# от списък от цели числа.
# Вход:
# numbers = [1,2,3,4,5,6,7,8,9]
# Изход:
# Number of even numbers: 4
# Number of odd numbers: 5

number_list =[] #съзваваме празен списък

# Колко числа ще въвеждате в списъка
x = int(input('Колко числа ще въвеждате в списъка = '))

# Попълване на списъка със целочислени числа
for i in range(x) :
    number_list.append(int(input(f'Въведете {i+1} естествено число от списъка=')))
print(f'Това е въведения списък с цели числа {number_list}')


even_counter = 0 # Брояч за четни числа
odd_counter = 0  # Брояч за нечетни числа
for i in range(x) : # цикъл за обхождане на списъка с числа
    if number_list[i] % 2 : # Проверка за четност ако остатъка е 1 то числото е нечетно 
        odd_counter += 1 # увеличаваме брояча на нечетните числа
    else:
        even_counter += 1 # увеличаваме брояча на четните числа
print(f'Броят на четните числа в списъка е {even_counter} а на нечетните е {odd_counter}')
