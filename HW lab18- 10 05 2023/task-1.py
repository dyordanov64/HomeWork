# Задача 1. Да се създаде .csv файл, който да пази информацията от таблицата. Файлът
# да се казва “Books.csv”

import csv

with open('Books.csv', mode = 'w', newline='') as f :
    writer = csv.writer(f, delimiter = ',')
    writer.writerow(['Book', 'Autor', 'Year Released'])
    writer.writerow(['To Kill A Moscingbird', 'Harper Lee', '1960'])
    writer.writerow(['A Brief History of Time', 'Stephen Hawking', '1988'])
    writer.writerow(['The Greath Gatsby', 'F.Scott Fitzgerald', '1922'])
    writer.writerow(['The Mah Who Mistook His Wife for a Hat', 'Oliver Sacks', '1985'])
    writer.writerow(['Pride and Predjudise', 'Jane Austen', '1813'])