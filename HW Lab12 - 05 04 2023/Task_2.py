# Задача 2. Да се промени горната задача така, че тя да връща стойност и след това да се
# принтира резултатът в зависимост от върната стойност от функцията. Да се напише и
# още една функция, която да принтира резултатът от търсенето.
# Вход: [1, 2, 5, 9, 10], 5 Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2 Изход: Not found


def List_search(List, Element) :
    if Element in List:
            return List.index(Element)

def print_search(x) :
    if x != None :
        print(f'Position {x}')
    else :
        print('Not Found')



List_1 = [1, 2, 5, 9, 10]

x = List_search(List_1, 3 )
print_search(x)

x = List_search(List_1, 5 )
print_search(x)
