# Задача 4. Да се създаде програма, която да чете цели числа въведени от потребителя,
# докато не бъде въведен празен ред. След като всичките числа са прочетени, програмата
# трябва да показва всички отрицателни числа, последвани от нули, последвани от всички
# положителни числа. Във всяка група номерата трябва да се показват в същия ред, в
# който са въведени от потребителя. Например, ако потребителят въведе стойностите 3, -
# 4, 1, 0, -1, 0 и -2, вашата програма трябва да изведе стойностите -4, -1, -2, 0, 0, 3 и 1 .
# Вашата програма трябва да показва всяка стойност на нов ред


List_of_Integers = []

# Цикъл за въвеждане на цели числа
while True :
    try :
        Int_Nomber = int(input('Input Integer Nomber or Enter = '))
        List_of_Integers.append(Int_Nomber)

    except :
        print('Изход от въвеждането ')
        break

# List_of_Integers=[-4, -3, -2, 0, 3, 5, 8, 0, -22, 13, -33]

print(List_of_Integers)
List_of_Integers.sort()
for i in range(len(List_of_Integers)) :
    print(List_of_Integers[i], end=' ')
    if (List_of_Integers[i] < 0) and (List_of_Integers[i+1] == 0) :
        print()
    elif List_of_Integers[i] == 0 and List_of_Integers[i+1] >0 :
        print()
        


# print(List_of_Integers)



