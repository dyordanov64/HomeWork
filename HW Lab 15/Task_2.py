# Задача 2. Декларирайте конструктор за класа Student, които да инициализира всички
# атрибути на класа. Данните за полетата, които не са известни трябва да се
# инициализират съответно със стойности с None, 0, или “”.

class Student :
	full_name = ''
	course = 2
	specialty = ''
	university = ''
	e_mail = ''
	tel_nomber = ''
	def __init__ (self, full_name, course, specialty, university, e_mail, tel_nomber ) -> None:
		self.full_name = full_name
		self.course = course
		self.specialty = specialty
		self.university = university
		self.e_mail = e_mail
		self.tel_nomber = tel_nomber

ivan = Student('Иван Стоянов Петков', 3, 'IT', 'Sofia University', 'ivan_petkov@abv.bg', '0888777632')
print(ivan.full_name)