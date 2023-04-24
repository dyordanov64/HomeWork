# Задача 2. Да се преработи следната задача, така че да използва речник. Да се напише
# програма, която да изчислява дневният калориен прием на даден потребител, като
# данните се въвеждат от клавиатурата. Необходимите данни са: възраст, пол (‘f’, ‘m’),
# височина (в сантиметри), тегло (в килограми), ниво на физическа активност (някоя от
# стойностите от 1 до 6 по-долу). Ниво на физическа активност се определя в следните
# няколко категории:
# 1 – базална метаболитна скорост
# 2 - заседнал – малка или никаква активност
# 3 - лека активност (1-3 пъти седмично) BMR * 1.2 BMR * 1.375
# 4 - средна активност(3-5 пъти седмично) BMR * 1.55
# 5 - висока активност (6-7 пъти седмично) BMR * 1.725
# 6-многовисокаактивност (6–7пъти седмично + тежка физическа работа). BMR*1.9
# Да се изчисли и какъв трябва да бъде дневният прием на калории ако:
# - за да запазите сегашното си тегло
# - за да сваляте по 0.5 кг на седмица
# - за да сваляте по 1 кг. на седмица
# - за да качвате по 0.5 кг. на седмица
# - за да качвате по 1 кг. на седмица
# Да се принтират данните на потребителя, както и калорийният прием спрямо горните
# няколко точки.
# Формула за изчисление на BMR при мъже:
# BMR = 66.47 + ( 13.75 × weight in kg ) + ( 5.003 × height in cm ) − ( 6.755 × age in years )
# Формула за изчисление на BMR при жени:
# BMR = 655.1 + ( 9.563 × weight in kg ) + ( 1.85 × height in cm ) − ( 4.676 × age in years )
# Пример:
# Входни данни:
# 29
# f
# 172
# 63.5
# 4
# Изход:
# Имате нужда от 2240 Калории на ден за да поддържате теглото си
# Имате нужда от 1740 Калории на ден за да сваляте по 0.5 кг на седмица
# Имате нужда от 1240 Калории на ден за да сваляте по 1 кг на седмица
# Имате нужда от 2740 Калории на ден за да качвате по 0.5 кг на седмица
# Имате нужда от 3740 Калории на ден за да качвате по 1 кг на седмица
# Пояснения:
# Години = 29
# Пол = “f”
# Ръст = 172
# Килограми = 63.5
# Ниво на активност = 4
# Изчисляваме BMR по формулата за жени:
# BMR = 655.1 + ( 9.563 * 63.5) + ( 1.85 * 172) − ( 4.676 * 29 ) = 1444.9465 калории
# Добавяме и активността на потребителя:
# Активността е 4 и гледаме по-нагоре каква е стойността за ниво 4. А тя е 1.55.
# BMR = BMR * 1.55 = 2239.6670750000003 = 2240 калории
# След това изчисляваме калориите какви трябва да са, ако искаме да сваляме килограми
# - при 0.5 кг седмица = BMR – 500 гр. = 1740 калории
# - при 1 кг на седмица = BMR – 1000 гр. = 1240 калории
# След това изчисляваме калориите какви трябва да са, ако искаме да качваме килограми
# - при 0.5 кг седмица = BMR + 500 гр. = 2740 калории
# - при 1 кг на седмица = BMR + 1000 гр. = 3240 калории

person_date = {
    
}
BMR = int()

actvity_level_dictionery = {
    '1' : 1,
    '2' : 1.2,
    '3' : 1.375,
    '4' : 1.55,
    '5' : 1.725,
    '6' : 1.9
}
# age = 0
# sex = ''
# height = 0
# weight = 0
# Activity_level = 0

while True :
    try :
        age=int(input('Моля въведете на колко години сте [1..150]='))
        if age in range(1, 150) :
            break
    except :
        continue

while True:
    sex = input('Моля въведете пол м/ж или m/f = ')
    if sex in ['m','f','м', 'ж', 'M', 'F', 'М', 'Ж'] :
        break


while True :
    try :
        height = int(input('Моля въдедете ръст в см [1..250]='))
        if height in range(1, 250) :
            # print(height)
            break
    except :
        continue

while True :
    try :
        weight = float(input('Моля въдедете тегло в кг [1..200] ='))
        if weight>1 and weight<250 :
            # print(weight)
            break
    except :
        continue

while True :
    try :
        Activity_level = input('Моля въведете вашето ниво на физическа активност [1..6]')
        if Activity_level in ['1','2','3','4','5','6'] :
            break
    except :
        continue

person_date['age'] = age
person_date['sex'] = sex
person_date['height'] = height
person_date['weight'] = weight
person_date['Activity_level'] = Activity_level

print(person_date)

if sex in ['f', 'ж', 'F', 'Ж'] :
    BMR = 655.1 + (9.563 * person_date['weight'] ) + (1.85 * person_date['height']) - (4.676 * person_date['age'])
else :
    BMR = 66.47 + ( 13.75 * person_date['weight'] ) + ( 5.003 * person_date['height'] ) - ( 6.755 * person_date['age'])

# добавяме коефициента за активност
BMR = BMR*actvity_level_dictionery[person_date['Activity_level']]


print(f'Имате нужда от {round(BMR)} калории на ден за да поддържате теглото си')
print(f'Имате нужда от {round(BMR-500)} Калории на ден за да сваляте по 0.5 кг на седмица')
print(f'мате нужда от {round(BMR-1000)} Калории на ден за да сваляте по 1 кг на седмица')
print(f'Имате нужда от {round(BMR+500)} Калории на ден за да качвате по 0.5 кг на седмица')
print(f'Имате нужда от {round(BMR+1000)} Калории на ден за да качвате по 1 кг на седмица')