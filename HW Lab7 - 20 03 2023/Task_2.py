# Задача 2. При анализиране на данни, събрани като част от научен експеримент, може
# да се наложи да се премахнат най-крайните (големите) стойности, преди да се
# извършват някакви други изчисления. Да се създаде списък от стойностите само с n на
# брой положителни числа. Трябва да се създаде ново копие на създаденият списък с
# премахнатите n най-големи елемента и n най-малките елементи. Редът на елементите
# във върнатия списък не трябва да съвпада с реда на елементите в първоначалния
# списък. Напишете програма, която да чете списък от числа въведени от потребителя и
# да премахва двете най-големи и двете най-малки стойности. Да се принтира новият
# списък, както и оригиналният. Програма трябва да генерира подходящо съобщение за
# грешка, ако потребителят въведе по-малко от 4 стойности.

list_of_pozitiv_integer = []
new_list_of_pozitive_integer = []
while True :
    try :
        x = int(input('Въведете цяло положително число за изход 0 = '))
        if x != 0 :
            print(len(list_of_pozitiv_integer))
            list_of_pozitiv_integer.append(x)
        elif len(list_of_pozitiv_integer) > 3 :
            break
        else :
            print('Не сте въвели минимум 4 числа')
    except :
        print('Не сте въвели коректно число')

print(f'оргиналния списък е {list_of_pozitiv_integer}')
list_of_pozitiv_integer.sort()
print(f'оргиналния сортиран списък е {list_of_pozitiv_integer}')
for i in range(2 , len(list_of_pozitiv_integer)-2) :
    new_list_of_pozitive_integer.append(list_of_pozitiv_integer[i])

print(f'новия списък без двете най-големи и двете най-малки числа е {new_list_of_pozitive_integer}')

