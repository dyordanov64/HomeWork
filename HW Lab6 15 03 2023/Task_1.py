# Задача 1. Да се напише програма, която да намира тези числа, които се делят на 7 и на
# 5, между 1500 и 2700.
br=0
for el in range(1500,2700):
    if not(el % 7) and not(el % 5) : # Проверка дали числото се дели едновременно на 5 и на 7 ако се дели се разпечатва числото
        print(el, sep=' ', end= ',')
        br +=1
print(f'Броя на тези числа е {br}')