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
	nimi=input("Siseta nimi: ")#вписываем име
	palga=input("Siseta palgad: ")#вписываем зарплату
	with open("inimesed.txt", "a") as inimesed: #добавляем человека в конец файла
		inimesed.write(nimi+"\n")#вписываем имя ноового человека 
	with open("palgad.txt", "a") as palgad: #добавляем зарплату в конец файла
		palgad.write(palga+"\n")#вписываем пароль ноового человека 
