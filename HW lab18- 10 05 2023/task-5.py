# Задача 5. Използвайки файла Books.csv, покажете всички данни, както и номерът на
# реда.

import csv

def print_book_csv(file_name, row_counter) :
    with open(file_name, mode='+r') as csvfile :
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader :
            row_counter += 1
            print(f'{row_counter}. {row}')

row_counter=0

print_book_csv('HomeWork\HW lab18- 10 05 2023\Books.csv', row_counter)
