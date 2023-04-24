# Задача 8. Напишете програма, която намира максималната редица от последователни
# нарастващи елементи в списък.
# Пример: {3, 2, 3, 4, 2, 2, 4} -> {2, 3, 4}.




list_of_nomber = []
max_broi_povtorenia = 0
list_increasing_numbers = []
max_len_list_inc_nombers = []


for i in range(len(list_of_nomber)) :
    if (i == 0 or list_of_nomber[i] > list_of_nomber[i-1]) :
        list_increasing_numbers.append(list_of_nomber[i])
        # print(f'индекса е {i} списъка е {list_increasing_numbers}')
    else :
        if len(max_len_list_inc_nombers) < len(list_increasing_numbers) :
            max_len_list_inc_nombers = list_increasing_numbers[:]
        # print(max_len_list_inc_nombers)
        list_increasing_numbers.clear()        
        list_increasing_numbers.append(list_of_nomber[i])



if len(max_len_list_inc_nombers) < len(list_increasing_numbers) :
    max_len_list_inc_nombers = list_increasing_numbers
print(f'списък на увеличаващите се елементи {max_len_list_inc_nombers}')
