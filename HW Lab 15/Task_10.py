# Задача 10. Към класа за мобилен телефон от предходните две задачи, добавете
# статично поле nokiaN95, което да съхранява информация за мобилен телефон модел
# Nokia 95. Добавете метод, в същия клас, който извежда информация за това статично
# поле.

class Mobilen_Telefon
    model = ''
    manufacturer = ''
    price = 0
    owner = ''
    nokiaN95 = 'Nokia N95'
    def __init__(self, mod:str,manuf:str, price:int,owner : str):
        self.model = mod
        self.manufacturer = manuf
        self.price = price
        self.owner = owner

    def print_n95(self):
        print(self.nokiaN95)



class Battery
    model = ''
    idle_time = 0
    hours_talk = 0

    def __init__(self, model:str, idle:int, hours:int):
        self.model = model
        self.idle_time = idle
        self.hours_talk = hours

class Screen
    size = 0
    color = 0
    def __init__(self, size:int, color:int):
        self.size = size
        self.color = color