from Funktsioonid import *
from too_failidega import *
import time
Admin=loe_failist_listisse("adminlog.txt")#Логин для входа в админ аккаунт
Inimesed=loe_failist_listisse("inimesed.txt")#Логины для обычного персонала
APasswords=loe_failist_listisse("administrator.txt")#Пароль для входа в админ аккаунт
Passwords=loe_failist_listisse("passwords.txt")#Пароль для входа в обычный аккаунт персонала

while True:#бексонечный цикл пока не выполнится действие до конца или пока не брейкнут
	print("Куда хотите войти?\nПользоватьель-[0]\nАдминистратор-[1]")
	v=int(input())#наш главный знак для взаимодействия
	print("Идет вход...\n")
	time.sleep(1.5)#временно приостанавилвает код(для эффекта)
	print("Синхронизация данных...\n")
	time.sleep(3.5)
	if v==0:#вход как обычный пользователь
		print("Вход Пользователя...")
		while 1:
			time.sleep(2)
			log=input("Введите логин:")
			if log in Inimesed:#Если log=логин есть в списке Inimesed то вы пройдете дальше
				print("Логин успешно введён.")
				break
			elif log not in Inimesed:#Если log=логина нет в списке Inimesed то цикл повторяется
				print("Не верный логин.")
		while 1:
			time.sleep(2)
			pas=input("Введите пароль:")
			if pas in Passwords:#Если pas=пароль есть в списке Passwords то вы пройдете дальше
				print("Вы вошли в систему.")
				break
			elif pas not in Passwords:#Если pas=пароля нет в списке Passwords то цикл повторяется
				print("Не верный пароль.")
	elif v==1:#вход как админ
		print("Вход Администрации...")
		while 1:
			time.sleep(2)
			log=input("Введите логин:")#Писать Sergei, другое не примит
			if log in Admin:#Если log=логин есть в списке Admin то вы пройдете дальше
				print("Логин успешно введён.")
				break
			elif log not in Admin:#Если log=логина нет в списке Admin то цикл повторяется
				print("Не верный логин.")
		while 1:
			time.sleep(2)
			pas=input("Введите пароль:")#Пароль 7493
			if pas in APasswords:#Если pas=пароль есть в списке APasswords то вы пройдете дальше
				print("Вы вошли в систему.")
				break
			elif pas not in APasswords:#Если pas=пароля нет в списке Passwords то цикл повторяется
				print("Не верный пароль.")
		break
while True:
	print("Что хотите посмотреть?\nCписок сотрудников-[0]\nЗарплата-[1]\nТоп сотрудников-[2]\nСредняя зарплата и какой человек ее получает-[3]")
	n=int(input())#наш главный знак для взаимодействия 2
	print("Загрузка...")
	time.sleep(2.5)
	if n==0:
		print("Вход в список сотрудников...")#Показывает вообщем сколько сотрудников и кем они работают
		time.sleep(1.5)
		with open("inimesed.txt", "r") as reader:#Читает содержимое файла и выводим на экран
			print(reader.read())
	elif n==1:
		print("Вход в систему зарплаты...")#Показывает зарплату сотрудников
		time.sleep(1.5)
		with open("money.txt", "r") as reader:
			print(reader.read())
	elif n==2:
		print("Вход в топ сотрудников...")#показывает топ богатых и бедных сотрудников 
		time.sleep(1.5)
		with open("top.txt", "r") as reader:
			print(reader.read())
	elif n==3:
		print("Среднюю зарплату и имя человека ее получающего...")#Показывает людей(2-ух) которые получают среднюю зарплату и как они наслаждаются ею
		time.sleep(1.5)
		with open("Normal_palgad.txt", "r") as reader:
			print(reader.read())
