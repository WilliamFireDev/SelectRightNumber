from randomint import *

print("Игра: ВЫБЕРИ ПРАВИЛЬНУЮ ЧИСЛО ЧТОБЫ ВЫЖИТЬ!")

#1 lvl 
playerSelect = input("Введите число(От 1 до 5): ")
con = int(playerSelect)

if con == k:
	print("Правильно!")
else: 
	print("Неправильно! Число было:" + str(k))


#2 lvl 
playerSelect2lvl = input("Введите число(От 1 до 6): ")
con2 = int(playerSelect2lvl)

if con2 == g:
	print("Правильно!")
else: 
	print("Неправильно! Число было:" + str(g))

#3 lvl 
playerSelect3lvl = input("Введите число(От 1 до 7): ")
con3 = int(playerSelect3lvl)

if con3 == j:
	print("Правильно!")
else: 
	print("Неправильно! Число было:" + str(j))

