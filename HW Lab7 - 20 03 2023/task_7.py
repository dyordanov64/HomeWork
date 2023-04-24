# Задача 7. Напишете програма, която намира максимална редица от последователни
# еднакви елементи в списък.
# Пример: {2, 1, 1, 2, 3, 3, 2, 2, 2, 1} -> {2, 2, 2}. ‘2’ * counter

list_of_nomber = []
max_broi_povtorenia = 0
Repeat_element = ''

while True :
    try :
        x = int(input('Въведете цяло число за формиране на списък или N изход:'))
        list_of_nomber.append(x)
    except :
        print('Натиснали сте изход')
        break

    for i in range(len(list_of_nomber)) :
        if list_of_nomber.count(list_of_nomber[i])> max_broi_povtorenia :
            max_broi_povtorenia = list_of_nomber.count(list_of_nomber[i])
            Repeat_element = list_of_nomber[i]

print(f'най-голям брой повторения {max_broi_povtorenia} има {Repeat_element} ')
