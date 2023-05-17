# Задача 3. Използвайки файла Books.csv, попитайте потребителя колко записи иска да
# добави в списък и след това му разрешете да добави още толкова. След като всички
# данни са добавени, попитайте потребителя да въведе автор и принтирайте всички
# книги за този автор. Ако в списъка няма книги от този автор, покажете подходящо
# съобщение.

import csv
def print_csv(file_name) :
    with open(file_name, mode='+r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
def search_book_of_autor(file_name, book_autor) :
    have_book = False
    with open('Books.csv', mode='+r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[1] == book_autor:
                have_book = True
                print(row[0])
        else:
            if not (have_book):
                print(f'Няма налични книги от този автор {book_autor}')
def input_book(file_name, nomber_books = int):
    for x in range(nomber_books):
        book_name = input('Input book name :')
        book_autor = input('Input book autor :')
        book_year_realised = input('Input book Year realised :')
        with open(file_name, mode='+a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow([book_name, book_autor, book_year_realised])

nomber_books = int(input('Kолко книги искате да добавите в списъка: '))
input_book('Books.csv', nomber_books)
print_csv('Books.csv')
book_autor = input('Input book autor :')
search_book_of_autor('Books.csv', book_autor)

