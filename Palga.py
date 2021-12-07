from Module import *
while True:
	b=input("Функции:\nДобавить персонал-[1]\nСамая большая запрала-[2]\nСамая маленькая зарплата-[3]\nСортировка-[4]\nВычисление средней зарплаты-[5]")
	if b=="1":
		add_person()
	elif b=="2":
		biggest_salary()
	elif b=="3":
		smallest_salary()
	elif b=="4":
		sorting()
	elif b=="5":
		keskmine()
	else:
		("Такой функции не существует")
