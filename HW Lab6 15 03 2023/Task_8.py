#  8. Да се принтира буквата A на екрана както е дадено по-долу

for i in range(1,6) :
    if i != 1 and i != 5 :
        print('*', sep='', end='')
    else :
        print(' ', sep='', end='')

print('')     # минава на нов ред

for j in range(1, 3) : # за два реда 
    for i in range(1,6) : # на 1 и 5 та позиция разпечатваме звездичка
        if i == 1 :
            print('*', sep='', end='')
        elif i == 5 :
            print('*', sep='', end='') # след 5 тия символ минава на нов ред
            print('')
        else :
            print(' ', sep='', end='') # за 2, 3, 4 позиция печата празен символ
    
print('*'*5) # разпечатва ред 5 позиции със звездички

for j in range(1, 4) : # Повтаря горния цикъл но за три реда
    for i in range(1,6) :
        if i == 1 :
            print('*', sep='', end='')
        elif i == 5 :
            print('*', sep='', end='')
            print('')
        else :
            print(' ', sep='', end='')
    


