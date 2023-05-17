# Задача 9. Декларирайте конструктор за всеки от създадените класове от предходната
# задача. Данните за полетата, които не са известни трябва да се инициализират
# съответно със стойности с None, 0, или “”.

class Mobilen_Telefon
    model = ''
    manufacturer = ''
    price = 0
    owner = ''

    def __init__(self, mod:str,manuf:str, price:int,owner : str):
        self.model = mod
        self.manufacturer = manuf
        self.price = price
        self.owner = owner


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