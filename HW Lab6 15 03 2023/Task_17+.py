# Задача 17. Да се напише програма, която да приема от клавиатурата цяло число n и като
# резултат да принтира всички числа до въведеното.
# Вход: n = 4 Вход: n = 11
# Изход: 1-2-3-4 Изход: 1-2-3-4-5-6-7-8-9-1-0-1-1
# Вход: n = 15
# Изход: 1-2-3-4-5-6-7-8-9-1-0-1-1-1-2-1-3-1-4-1-5
# какво означава всички числа до въведеното

Number_integer = 0

while True :
    try :
        Number_integer = int(input('Input integer nomber='))
        break
    except :
        print('You did not enter an integer ')

for i in range(1,Number_integer+1) :
    if i != Number_integer :
        print(i,end='-')
    else :
        print(i)
    

