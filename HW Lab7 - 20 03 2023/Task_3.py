# Задача 3. Да се създаде програма, която чете думи като вход от клавиатурата, докато
# потребителят не въведе празен ред. След като потребителят въведе празен ред,
# програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж.
# Думите трябва да се показват в същия ред, в който са били въведени. Например, ако
# потребителят въведе:
# first
# second
# first
# third
# second
# тогава програмата трябва да принтира само:
# first
# second
# third

List_of_words =['new', 'york', 'news', 'paper', 'new']
New_List = []

# Запълване на списък от думи докато не не въведе празен ред
# while True :
#     word = input('Въведете дума и натиснете Enter = ')
#     if word == '' :
#         break
#     else :
#         List_of_words.append(word)

# for i in range(len(List_of_words)) :
    
#     for j in range(i+1,len(List_of_words)) :
#         print(i,j)
#         if List_of_words[i] == List_of_words[j] :
#             List_of_words.pop(j)
#         continue

# print(f'това е списъка от думи {List_of_words}')
# print(New_List)

for i in range(len(List_of_words)) :
 print(len(List_of_words))
 print(List_of_words.count(List_of_words[i]))



