# Задача 6. Да се напише програма, която генерира всички подсписъци на даден списък.
# Например, списъците на [1, 2, 3] са [], [1], [2], [3], [1, 2], [2, 3], [1, 3] и [1, 2, 3]. 

# Въвеждане на списък от цели числа
List_of_Nombers =[3, 5, 2]
Sublist_of_List_of_Nombers = []

# while True :
#     try :
#         x = int(input('Въведете цяло число за формиране на списък или N изход:'))
#         List_of_Nombers.append(x)
#     except :
#         print('Натиснали сте изход')
#         break

print(List_of_Nombers)
print(Sublist_of_List_of_Nombers)
for i in range(len(List_of_Nombers)) :
    Sublist_of_List_of_Nombers.append(List_of_Nombers[i])
    print(Sublist_of_List_of_Nombers, f'i= {i}')
    Sublist_of_List_of_Nombers.clear()
for i in range(len(List_of_Nombers)-1) :
    Sublist_of_List_of_Nombers.append(List_of_Nombers[i])
    print(Sublist_of_List_of_Nombers, f'i= {i}')    



    # j = i + 1
    # while j < len(List_of_Nombers) :
    #     Sublist_of_List_of_Nombers.append(List_of_Nombers[j])
    #     print(Sublist_of_List_of_Nombers, f'j= {j}')
    #     k=j + 1
    #     while k < len(List_of_Nombers) :
    #         Sublist_of_List_of_Nombers.append(List_of_Nombers[k])
    #         print(Sublist_of_List_of_Nombers, f'k= {k}')
    #         Sublist_of_List_of_Nombers.clear()
    #         k += k

    
    
    # # Sublist_of_List_of_Nombers.append(List_of_Nombers[i])
    # for j in range(i,len(List_of_Nombers)) :
    #     Sublist_of_List_of_Nombers.append(List_of_Nombers[j])
    #     print(Sublist_of_List_of_Nombers)
    #     # Sublist_of_List_of_Nombers = []
    #     for k in range(j, len(List_of_Nombers)) :
    #         Sublist_of_List_of_Nombers.append(List_of_Nombers[k])
    #         print(Sublist_of_List_of_Nombers)
    #         # Sublist_of_List_of_Nombers = []


        
       



