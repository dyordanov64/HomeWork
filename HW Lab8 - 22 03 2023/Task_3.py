# Задача 3. Да се създаде речник, който да съдържа информацията за дадено меню на
# ресторант. Ключовете му трябва да са стрингове, а стойностите цените. Програмата ще
# по иска от потребителя да въведе следната информация:
# - Ако потребителят въведе името на дадено ястие от менюто, тогава програмата
# да принтира цената и колко е общата цена до момента. След това да пита
# отново дали потребителят не иска да въведе нещо друго.
# - Ако потребителят въведе име на ястие, което не е в менюто, тогава програмата
# да изведе подходящо съобщение. След което отново програмата да пита
# потребителя да избере нещо друго от менюто.
# - Ако потребителят въведе празен стринг, тогава програмата да спре да подканва
# потребителя да избира от менюто и да изведе на екрана общата крайна сума.
# Пример:
# Order: sandwich
# sandwich costs 10, total is 10
# Order: tea
# tea costs 7, total is 17
# Order: elephant
# Sorry, we are fresh out of elephant today. Order: <enter>
# Your total is 17

menu = {
    'sandwich': 10,
    'burger' : 15,
    'chkembe': 3,
    'coca-cola': 5,
    'beer': 11    
}

# Разпечатваме менюто за да го вижда потребителя
for dich, cost in menu.items() :
    print(dich, cost)
total = 0
# цикъв за въвеждане на озбора от потребителя
while True :
    dish = input('Would you like something from the menu, your order? =')
    if dish in menu :
        total = total + menu[dish]
        print(f'{dish} cost {menu[dish]}, total is {total} ')
    elif dish == '' : # при избор празен стринг се излиза от цикъла
        break
    else :
        print('Sorry, we are fresh out of elephant today.') # при грешен избор връщане към нов избор
    

print(f'Your total is {total}')