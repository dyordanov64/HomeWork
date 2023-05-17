# Задача 11. Добавете изброим тип BatteryType, който съдържа стойности за тип на
# батерията (Li-Ion, NiMH, NiCd, …) и го използвайте като ново поле за класа

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
    battery_type = [LiIon, NiMH, NiCd]

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