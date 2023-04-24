# Задача 15. Да се напише програма, която подканва потребителя да въведе число и
# програмата да провери дали то е просто или не.
# Вход:
# Please enter a number
# >>> 12
# Изход:
# The number is not prime.

broiach = 0
while True :
    number = int(input('моля въведете число ='))
    for i  in range(1,number+1) : # цикъл за увеличаване на числото за проверка дали въведеното число се дели на някое друго освен на 1 или себе си
        # print(i)
        if not(number % i) :
            broiach += 1 # когато въведеното число се дели на някое число от 1 до себе си се увеличава брояча
            #print(broiach)
    # print(f'Брояча е {broiach}')

    if broiach != 2 : # Когато въведеното число се е делило на повече числа от 1 и себе си т.е брояча е >2 не е просто
        print('The number is not prime')
    else :
        print('The number is prime')
    
    break

