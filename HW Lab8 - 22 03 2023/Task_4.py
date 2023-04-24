# Задача 4. Да се напише програма, която да проследява валежите в редица градове.
# Потребителят да може да въвежда името на град; ако името на града е празно,
# програмата излиза и принтира отчет. Ако името на града не е празно, потребителят
# ще трябва да въведе информация за количеството дъжд за конкретният
# град(обикновено се измерва в милиметри). След въвеждане на количеството дъжд,
# потребителят има възможност да въвежда следващ град и количество дъжд и това
# ще го прави докато не натисне „Enter“, вместо да напише името на града.
# Пример:
# Boston
# 5
# New York
# 7
# Boston
# 5
# [Enter; blank line]
# Изход:
# Boston: 10
# New York: 7

cities_and_rainfall ={

}

while True :
    city = input('Please input city name = ')
    if city == '' :
        break
    rain = int(input ('Please insert amount of precipitation in mm = '))
    cities_and_rainfall.update({city : rain})

for city, rain in cities_and_rainfall.items() :
    print(city,rain)
