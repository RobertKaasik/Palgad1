from Funktsioonid import *
from too_failidega import *
import time

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
