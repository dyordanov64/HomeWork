# програма за извеждане на определение дебелината на човек чрез пресмятане на BMI
weight = int( input('Enter a Integer number for the weight in kg. =')) # Въвжедане теглото на човека в кг
height =float( input('Enter a number for the height m. =')) # Въвеждане височината на човека в метри
BMI = round(weight/(height*height),1)
# print(BMI)


if BMI <= 18.5 : # ако индекса е <= 18.5 се изписва Underweight
    print('The person with the entered weight {} and height {} is'.format(weight,height ) + ' Underweight')
elif BMI > 18.5 and BMI <= 24.9: # ако индекса е в диапазона <= 18.5 се изписва Underweight
    print('The person with the entered weight {} and height {} is'.format(weight,height ) + ' Normal')
elif BMI >= 25 and BMI <= 29.9:
    print('The person with the entered weight {} and height {} is'.format(weight,height ) + ' Overweight')
else : 
    print('The person with the entered weight {} and height {} is'.format(weight,height ) + ' Obesity')
