# Задача 5. Да се напише програма, която да намира разликата между два речника.
# Като резултат програмата да генерира нов речник, който да съдържа разликата
# между двата речника. Ако няма разлика между речниците да се принтира празен
# речник. За всяка двойка ключ-стойност, която се различава, да се запазят
# различаващите се стойности в списък, а списъкът да се запази в речник, като
# ключът да съвпада с текущият. Ако някой от речниците не съдържат даденият
# ключ, то в списъкът, той трябва да бъде записан като None.
# Вход: Вход: Вход:
# d1 = {'a':1, 'b':2, 'c':3} d3 = {'a':1, 'b':2, 'd':3} d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'a':1, 'b':2, 'c':4} d4 = {'a':1, 'b':2, 'c':4} d5 = {'a':1, 'b':2, 'd':4}
# Изход: Изход: Изход:
# {'c': [3, 4]} {'c': [None, 4], 'd': [3, None]} {'c': [3, None], 'd': [None, 4]}
# Вход: d1 = {'a':1, 'b':2, 'c':3} и d1 = {'a':1, 'b':2, 'c':3}
# Изход: {}

# d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'a':1, 'b':2, 'c':4}
# d1 = {'a':1, 'b':2, 'd':3}
# d2 = {'a':1, 'b':2, 'c':4}
d1 = {'a':1, 'b':2, 'd':4}
d2 = {'a':1, 'b':2, 'd':4}
output_d = {}
x=''

for key, value in d1.items() :
    # print(d2[key])
    
    if not key in d2 : 
        x= d2.get(key, "none")
        print(x)
        # print(d1[key], ' ', d2[x])
        output_d.update({key:[d1[key], 'None']})
        for key1, value1 in d2.items() :
            if not key1 in d1 :
                output_d.update({key1:[d2[key1], 'None']})

    else :
        if d1[key] != d2[key] :
            print(d1[key], ' ', d2[key])
            output_d.update({key:[d1[key], d2[key]]})
        # output_d.update(key:x)
    # elif d1[key] != d2[key]
    #     output_d.update

print(output_d)   
        