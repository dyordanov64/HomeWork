# Задача 14. Да се напише програма, която да генерира число на случен принцип и да
# подкани потребителя да познае това число. Да извежда следните стойности too low, too
# high, или exactly right, в случай, че потребителя е познал, или не числото.
import random

random_number = random.randint(1, 100)
print()
while (True) :
    x = int(input('Моля познайте какво число е избрал компютъра = '))
    if x < random_number :
        print('too low')
    elif x > random_number :
        print('too high')
    else :
        print('exactly right')
        break
