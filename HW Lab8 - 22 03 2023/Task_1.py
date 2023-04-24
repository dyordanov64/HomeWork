# Задача 1. Да се преработи следната задача, така че да използва речник.
# Напишете програма, която преобразува дадено число в интервала [0..999] в текст,
# съответстващ на българското произношение. Примери:
# -0 -> “Нула”
# -273 -> ”Двеста седемдесет и три”
# -400 -> ”Четиристотин”
# -501 -> “Петстотин и едно”
# -711 -> “Седемстотин и единадесет”

desetici =int()
stotici = int()
edinici = int()

nomber = input('Въведете цяло число от 0..999=')

Nombers = {
    '0' : 'нула',
    '1' : 'едно',
    '2' : 'две',
    '3' : 'три',
    '4' : 'четири',
    '5' : 'пет',
    '6' : 'шест',
    '7' : 'седем',
    '8' : 'осем',
    '9' : 'девет',
    '10' : 'десет',
    '11' : 'единадесет',
    '12' : 'дванадесет',
    '13' : 'тринадесет',
    '14' : 'четиринадесет',
    '15' : 'петнадесет',
    '16' : 'шестнадесет',
    '17' : 'седемнадесет',
    '18' : 'осемнадесет',
    '19' : 'деветнадесет',
    '20' : 'двадесет',
    # '21' : 'двадесет и едно',
    # '12' : 'двадесет и две',
    # '13' : 'двадесет и три',
    # '24' : 'двадесет и четири',
    # '25' : 'петнадесет',
    # '26' : 'шестнадесет',
    # '27' : 'седемнадесет',
    # '28' : 'осемнадесет',
    # '29' : 'деветнадесет'

}

# for i in range(3) :
stotici = int(nomber)//100
# print(stotici)
# print(Nombers[str()],'стотин', sep='')
x = int(nomber) % 100 # остатъка след делението на 100
print(x)
desetici = int(x)//10
print(desetici)
edinici = int(x)%10   # остатъка след делението на 10 т.е. това са единиците

if stotici == 1  :
     print('сто', sep='', end = ' ')
elif stotici == 2 or stotici == 3 :
    print(Nombers[str(stotici)],'ста', sep='', end = ' ')
elif stotici != 0 :     
     print(Nombers[str(stotici)],'стотин', sep='', end = ' ')

if  desetici > 2 :
    print(Nombers[str(desetici)],'десет', sep = '', end = ' ')
    
else :
    if desetici == 2 :
        print('двадесет', sep = '', end = ' ')
        print('и ',Nombers[str(edinici)],'', sep = '', end = ' ') 
    elif desetici == 1 :
        if stotici != 0  :
            print('и ',Nombers[str(x)], sep = '', end = ' ')
        else :
            print(Nombers[str(x)], sep = '', end = ' ')
    else :
        if edinici != 0 :   
            print('и ',Nombers[str(edinici)],'', sep = '', end = ' ') 
        else :
            print(Nombers[str(edinici)],'', sep = '', end = ' ') 

# if edinici != 0 :   
#     print('и ',Nombers[str(edinici)],'', sep = '', end = ' ') 



