# Задача 18. Да се напише програма, която да приема като вход текст и да намира
# количеството знаци в текста. Включват се интервалите и текста трябва да е с малки
# букви. Ако няма дубликати, да се принтира 0.
# Вход: Hello World! Вход: foobar Вход: birthday Вход: helicopter
# Изход: 3 Изход: 1 Изход: 0 Изход: 1

# Според мен условието е някак си странно най-вероятно трябва да се броят повтарящите се знаци в текста

text=''
text_repeat=''
broyach1=0
broyach2=0
text= input('Input String=')

for i in range(len(text)) :
    for j in range(len(text)-i) :
        if text[i] == text[j] :
            broyach1 +=1
            
    if broyach1 > broyach2 : 
        text_repeat=text[i]
        broyach2 = broyach1
    broyach1 = 0

print(f'повтарящ се символ {text_repeat}')
print(broyach2)

