# Задача 1. Да се напише функция, която да търси в списък. Като параметър да приема
# списък и да принтира ако елементът е в списъка неговата позиция, ако ли не да
# принтира, че не е намерен.
# Вход: [1, 2, 5, 9, 10], 5 Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2 Изход: Not found


def List_search(list_in, Element) :
    # for i in range(len(list_in)) : 
    #     if Element == list_in[i] :
    #         pos = i
    # if print(f'Position {pos}')
    # print('Not Found')
    print(f'Input list {list_in}')
    if Element in list_in :
        print(f'Searching Element {Element} in Position {list_in.index(Element)}')
    else :
        print(f'Елемента {Element} - Not Found')




List_1 = [1, 2, 5, 9, 10]

List_search(List_1, 3)
List_search(List_1, 5)

