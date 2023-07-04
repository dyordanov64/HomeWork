# Задача 4. Използвайки файла Books.csv, помолете потребителя да въведе начална и
# крайна година. Покажете всички книги, издадени между тези две години.

import csv

def search_book_of_years(file_name, year1, year2) :
    have_book = False
    with open(file_name, mode='+r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[2] >= year1 and row[2]<=year2:
                have_book = True
                print(row[0])
        else:
            if not (have_book):
                print(f'Няма налични книги този диапазон от години {year1} - {year2}')

year1 = input('Въведете начална година:')
year2 = input('Въведете крайна година:')
search_book_of_years('HomeWork\HW lab18- 10 05 2023\Books.csv', year1, year2)