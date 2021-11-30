from Funktsioonid import *
from too_failidega import *
import time
Admin=loe_failist_listisse("adminlog.txt")
Inimesed=loe_failist_listisse("inimesed.txt")
Palgad=loe_failist_listisse("palgad.txt")
APasswords=loe_failist_listisse("administrator.txt")
Passwords=loe_failist_listisse("passwords.txt")

while True:
	print("Куда хотите войти?\nПользоватьель-[0]\nАдминистратор-[1]")
	v=int(input())
	print("Идет вход...\n")
	time.sleep(1.5)
	print("Синхронизация данных...\n")
	time.sleep(3.5)
	if v==0:
		print("Вход Пользователя...")
		while 1:
			time.sleep(2)
			log=input("Введите логин:")
			if log in Inimesed:
				print("Логин успешно введён.")
				break
			elif log not in Inimesed:
				print("Не верный логин.")
		while 1:
			time.sleep(2)
			pas=input("Введите пароль:")
			if pas in Passwords:
				print("Вы вошли в систему.")
				break
			elif pas not in Passwords:
				print("Не верный пароль.")
	elif v==1:
		print("Вход Администрации...")
		while 1:
			time.sleep(2)
			log=input("Введите логин:")#Писать Sergei, другое не примит
			if log in Admin:
				print("Логин успешно введён.")
				break
			elif log not in Admin:
				print("Не верный логин.")
		while 1:
			time.sleep(2)
			pas=input("Введите пароль:")#Пароль 7493
			if pas in APasswords:
				print("Вы вошли в систему.")
				break
			elif pas not in APasswords:
				print("Не верный пароль.")
		break
while True:
	print("Что хотите посмотреть?\nCписок сотрудников-[0]\nЗарплата-[1]\nТоп сотрудников-[2]")
	n=int(input())
	print("Загрузка...")
	time.sleep(2.5)
	if n==0:
		print("Вход в список сотрудников...")
		time.sleep(1.5)
		with open("inimesed.txt", "r") as reader:#Читает содержимое файла и выводим на экран
			print(reader.read())
	elif n==1:
		print("Вход в систему зарплаты...")
		time.sleep(1.5)
		with open("money.txt", "r") as reader:
			print(reader.read())
	elif n==2:
		print("Вход в топ сотрудников...")
		time.sleep(1.5)
