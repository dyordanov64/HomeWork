# Задача 4. Добавете метод в класа Student, който извежда пълна информация за
# студента.
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

	def print_all_student_info(self) :
		print(self.full_name, self.course, self.specialty, self.university, self.e_mail, self.tel_nomber,sep='\n')
		
ivan = Student('Иван Стоянов Петков', 3, 'IT', 'Sofia University', 'ivan_petkov@abv.bg', '0888777632')
petar = Student('Петър Стоянов Петров', 2, 'philosophy', 'Sofia University', 'petar_stoianov@abv.bg', '0888777666')
ivan.print_all_student_info()
print()
petar.print_all_student_info()
