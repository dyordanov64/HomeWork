# Задача 2. Използвайте създаденият файл Books.csv и накарайте потребителя да добави
# нов запис след всички останали редове във файла. Да се принтират всички редове от
# файла на отделен ред.

import csv


book_name = input('Input book name :')
book_autor = input('Input book autor :')
book_year_realised = input('Input book Year realised :')

with open('Books.csv', mode='+a', newline='') as f :
    writer = csv.writer(f, delimiter=',')
    writer.writerow([book_name, book_autor, book_year_realised])

with open('Books.csv', mode='+r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)