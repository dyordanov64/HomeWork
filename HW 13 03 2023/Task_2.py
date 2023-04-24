#  Да се състави програма, чрез която се въвеждат 2 естествени двуцифрени
# числа a,b. Програмата да изведе съобщение дали последната цифра от произведението
# на двете числа е четна, както и самата цифра. Входни данни: a,b - естествени числа от
# интервала [10..99].
# Използвайте проверка на логическо условие - оператор if.
# Пример: 15, 25 Изход: 375, 5 нечетна

# Проверка за коректност на първото въведено число
try :
    Number_1_of_2_digits = int(input("Въведете първо двуцифрено цяло число от интервала [10..99] = "))
    if Number_1_of_2_digits < 10 or Number_1_of_2_digits >99 :
        raise
except :
    print(f'Въвели сте некоректна стойност за първото двуцифрено число {Number_1_of_2_digits}')
    exit()
# Проверка за коректност на второто въведено число
try :
    Number_2_of_2_digits = int(input("Въведете второ двуцифрено цяло число от интервала [10..99] = "))
    if Number_2_of_2_digits < 10 or Number_2_of_2_digits >99 :
        raise
except :
    print(f'Въвели сте некоректна стойност за второто двуцифрено число {Number_2_of_2_digits}')
    exit()  

#  Да намерим последната цифра на произведението на двете числа
product_of_the_two_numbers = Number_1_of_2_digits * Number_2_of_2_digits
String_product_of_the_two_numbers = str(product_of_the_two_numbers) # произведението превръщаме в стринг за да можем да вземем последната цифра
# length = len(String_product_of_the_two_numbers)
# print(length)
last_digit = String_product_of_the_two_numbers[len(String_product_of_the_two_numbers)-1] # взимаме последната цифра от произведението
# print(String_product_of_the_two_numbers, last_digit)
if int(last_digit) % 2 : # когато модула от деленето на 2 е <> 0 т.е. True последата цифра е нечетна
    print(f'Произведението на двете числа е {product_of_the_two_numbers} последната цифра на произведението е {last_digit} и е нечетна')    
else : # когато остатъка е = 0 резултата е False последната цифра е четна
    print(f'Произведението на двете числа е {product_of_the_two_numbers} последната цифра на произведението е {last_digit} и е четна')