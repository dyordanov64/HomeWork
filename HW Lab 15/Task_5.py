# Задача 5. Модифицирайте текущия код на класа Student така, че да капсулирате данните
# в класа чрез свойства.


class Student :
	counter = 0
	full_name = ''
	course = 2
	specialty = ''
	university = ''
	e_mail = ''
	tel_nomber = ''
	def __init__(self, full_name:str, course:int, specialty:str, university:str, e_mail:str, tel_nomber:str ) -> None:
		self.full_name = full_name
		self.course = course
		self.specialty = specialty
		self.university = university
		self.e_mail = e_mail
		self.tel_nomber = tel_nomber
		Student.counter += 1
		
	def setFullName(self,full_name:str) :
		self.full_name = full_name
	
	def setCourse(self,course:str) :
		self.course = course
	
	def setUniversity(self, university :str) :
		self.university = university

	def setSpecialty(self, specialty : str) :
		self.specialty = specialty
		
	def setEmail(self, e_mail : str) :
		self.e_mail = e_mail

	def setTelefon(self, tel_nomber : str) :
		self.tel_nomber = tel_nomber

	def print_all_student_info(self) :
		print(self.full_name, self.course, self.specialty, self.university, self.e_mail, self.tel_nomber,sep='\n')

	
	def getFullName(self) :
		return self.full_name
	
	def getCourse(self) :
		return self.course
	
	def getUniversity(self) :
		return  self.university

	def getSpecialty(self) :
		return self.specialty
		
	def getEmail(self) :
		return self.e_mail

	def getTelefon(self) :
		return self.tel_nomberreturn 
		
ivan = Student('Иван Стоянов Петков', 3, 'IT', 'Sofia University', 'ivan_petkov@abv.bg', '0888777632')
petar = Student('Петър Стоянов Петров', 2, 'philosophy', 'Sofia University', 'petar_stoianov@abv.bg', '0888777666')

print(ivan.getFullName(),ivan.getCourse(),ivan.getSpecialty(),ivan.getUniversity(), ivan.getEmail(),ivan.getUniversity(), sep = '\n')
