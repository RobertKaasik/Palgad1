def lists()->list:#делаем лист из людей и зарплаты
	salary=[]
	with open("salary.txt", "r") as f1: #открывает файл
		for s in f1:
			salary.append(s.strip())
	human=[]
	with open ("human.txt", "r") as inimene:#открывает файл
		for q in inimene:
			human.append(q.strip())
	return salary,human#Возвращает функции

def add_person ():#добавляет людей и зарплату
	name=input("Введите име: ")#вписываем име
	salarys=input("Введите зарплату: ")#вписываем зарплату
	with open("human.txt", "a") as human: #добавляем человека в конец файла
		human.write(nimi+"\n")#вписываем имя ноового человека 
	with open("ssalary.txt", "a") as salary: #добавляем зарплату в конец файла
		salary.write(palga+"\n")#вписываем пароль ноового человека

def biggest_salary():#самая большая зарплата
	salary,human=lists()#приравниваем к списку
	suur=max(salary) # Ищим большое число и приравниванием его к переменной
	a=salary.index(suur) # индекс = переменной
	print("Самая большая зарплата у "+inimesed[a]+" зарплата")
	
def smallest_salary():#самая маленькая зарплата
	salary,human=lists()
	salaryS=salary.copy()
	salaryS.sort()
	b=salaryS[0]
	a=salary.index(a)
	print("Самамя маленькая зарплата у "+inimesed[b]+" зарплата составляет "+ palgadS[0]+" евро")

def sorting():#Сортировка зарплат и имен(лестничным виде)
	salaryS=[]
	salary,human=lists()
	salaaryS=ssalary.copy()
	salarydS.sort()
	for palk in salaryS:
		b=salary.index(palk) # ищем индекс по переменной и приравниваем к другой переменной чтобы найти имя и зарплату в несортированых списках
		print(salary[a]+" "+human[a])
def centre():#вычисление средней зарплаты
	salary,human=lists()
	summa=0#начальная сумма 0
	for palk in salary:
		summa+=float(palk)#вычисляем средную зарплату(начало)
	centre=summa/len(salary)#Вычисляет зарплату(конец)
	print("Средняя зарплата "+centre)
	differences=0
	if centre in palgad:
		centre=human[palgad.index(centre)]
		print(centre)
	else:
		centre="Отсутствует"
		print(centre)