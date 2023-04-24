# Задача 7. Да се напише програма, която принтира редицата на Фибуначи между 0 и 50.
# Редицата на Фибуначи е: 0, 1, 1, 2, 3, 5, 8, 13, 21, … Всяко следващо число е сумата от
# предходните две.
# Изход: 1 1 2 3 5 8 13 21 34

Fibunacci_series=[]

x=50
# формулата на Фибуначи F(n) = F(n-1) + F(n-2) където F(0) = 0 F(1) = 1
for i in range(x) :
    if i==0  : 
        Fibunacci_series.append(0)
    elif i==1 :
        Fibunacci_series.append(1)
    else :
        if (Fibunacci_series[i-2]+Fibunacci_series[i-1]) < x   :
            Fibunacci_series.append(Fibunacci_series[i-2]+Fibunacci_series[i-1])
        else :
            break
        
print(Fibunacci_series)
