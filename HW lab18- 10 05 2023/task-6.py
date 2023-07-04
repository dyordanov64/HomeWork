# Задача 6. Импортирайте данните от файла Books.csv в списък. Покажете списъка на
# потребителя. Помолете го да избере ред от списъка, който да бъде изтрит, и го
# премахнете от списъка. Попитайте потребителя, кои от данни, той иска да бъдат
# променени и го направете. Запишете данните обратно в оригиналния .csv файл, като
# презапишете съществуващите данни с променените данни.

import csv 

row_count = 0
with open('HomeWork\HW lab18- 10 05 2023\Books.csv', mode='r') as csvfile :

    data=list(csv.reader(csvfile, delimiter= ','))
    for el in data :
        if row_count==0 :
            el.insert(0,'ID')
            row_count += 1
        else :
            el.insert(0,row_count)
            row_count += 1
        print(el)

print(data,sep= "\n")


data_row = int(input(f'Въведете номер на ред който да бъде изтрит 0-{len(data)-1}:'))

data.pop(data_row-1)
# print(data, sep='\n')

