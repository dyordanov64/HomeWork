# Задача 3. Добавете статично поле в класа Student, в което се съхранява броя на
# създадените обекти от този клас.
class Student :
	counter = 0
	full_name = ''
	course = 2
	specialty = ''
	university = ''
	e_mail = ''
	tel_nomber = ''
	def __init__(self, full_name, course, specialty, university, e_mail, tel_nomber ) -> None:
		self.full_name = full_name
		self.course = course
		self.specialty = specialty
		self.university = university
		self.e_mail = e_mail
		self.tel_nomber = tel_nomber
		Student.counter += 1
		
ivan = Student('Иван Стоянов Петков', 3, 'IT', 'Sofia University', 'ivan_petkov@abv.bg', '0888777632')
petar = Student('Петър Стоянов Петров', 2, 'philosophy', 'Sofia University', 'petar_stoianov@abv.bg', '0888777666')
print(ivan.full_name)
print(Student.counter)