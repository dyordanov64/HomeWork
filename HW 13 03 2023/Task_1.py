#  Да се състави програма, чрез която се въвежда 4-цифренo естествено число от
# интервала [1000.. 9999]. От това число се формират 2 нови 2-цифрени числа. Първото
# число се формира от 1-та и 4-та цифра на въведеното число. Второто число се формира
# от 2-рa - 3-та цифра на въведеното число. На екрана да се изведе дали 1-то ново число
# e по-малко <, равно = или по-голямо от 2-то число.
# Използвайте проверка на логическо условие - оператор if.
# Пример: 3332 Изход: по-малко (32<33)
# Пример: 1144 Изход: равни (14=14)
# Пример: 9875 Изход: по-голямо (95>87)

try : # проверка за коректно въведено 4 цифрено естественочисло
    Number_4_digit = input('Въведете 4 цифрено естествено число в интервала [1000..9999]=')
    int(Number_4_digit)
    # print(len(Number_4_digit))
    if len(Number_4_digit)< 4 or len(Number_4_digit)>4 :
        raise # Exception("Разрешени са само числа в интервала [1000..9999]")
    #
except :  #Exception as ex :
    #print(ex)
    print('Въвели сте неправилна стойност или число извън интервала [1000..9999]')
    exit()

a2 = (Number_4_digit[1]) #взимаме 2-та цифра на въведеното число
a1 = (Number_4_digit[0]) #взимаме 1-ва цифра на въведеното число
a3 = (Number_4_digit[2]) #взимаме 3-та цифра на въведеното число
a4 = (Number_4_digit[3]) #взимаме 4-та цифра на въведеното число


# формираме 2 двуцифрени числа съответно първото от 1-ва и 4-та цифра и второ от 2-ра и 3-та цифра на въведеното четирицифренно число
Number_1_4 = int(a1+a4) # създаваме ново число от 1 и 4 та цифра
Number_2_3 = int(a2+a3) # създаваме ново число от 2 и 3 та цифра

# Проверка новите двуцифрени числа какви са едно спрямо друго >, = или < и извеждане на съответни съобщения

if Number_1_4 < Number_2_3 :
    print(f'{Number_1_4} < {Number_2_3}')
elif Number_1_4 == Number_2_3 :
    print(f'{Number_1_4} = {Number_2_3}')
else :
    print(f'{Number_1_4} > {Number_2_3}')