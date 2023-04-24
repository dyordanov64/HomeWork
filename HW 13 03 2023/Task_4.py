# Съставете програма, която по въведено трицифренo число проверява дали
# числото се дели на всяка своя цифра. Във въведеното число да няма цифра 0.
# Използвайте проверка на логическо условие - оператор if.
# Пример: 121 Изход: 1:2:4 дели се

try:
	x = input('Въведете 1 трицифренно число, което да не съдържа 0: ')

	if ('0' in x) or (len(x)!=3):
		raise
except:
	print('Въвели сте грешни данни или число с повече от 3 цифри')
	exit()


### дали числото се дели на всяка своя цифра.
## get digits from x:
a1 = int(x[0])
a2 = int(x[1])
a3 = int(x[2])
x=int(x)

## check if x is deleted on each digits
if x%a1 == 0 and x%a2 == 0 and x%a3 == 0:
	print(f'{a1}:{a2}:{a3} дели се')
else:
	print(f'Числото {x}  Не се дели!')
