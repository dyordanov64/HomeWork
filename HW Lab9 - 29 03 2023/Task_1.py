# Задача 1. Да се напише програма, която сортира в нарастващ ред списък, чиито елементи
# са tuples. При сортирането да се взема предвид последният елемент във всеки tuple. В
# списъкът не трябва да се съдържат празни tuples.
# Вход: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Изход: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list2 = []
print(f'оргиналния списък е {list1}')

# min = list1[0]
# print(type(min))

# цикъл за добавяне на елементи в list2
for ind in range(len(list1)) :
    min=list1[0]
    # цикъл за намиране на най малкия елемент на list1
    for x in list1 :
        
        if x[1] < min[1] :
            min = x
            
    list1.pop(list1.index(min)) # премахваме най-малкия елемнт от list1 
    list2.append(min) # и го добавяме в list2
    # print(list1, list2)
    
print(f'сортирания списък е {list2}')
