# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# candies = 2021
# print(f'{candies} всего конфет')
# count = randint(1, 2)
# while candies > 0:
# count += 1
# if count % 2 == 0:
# print('ходит игрок 2')
# else:
# print('ходит игрок 1')
# quantity = int(input('Введите число конфет которое изымаете - '))
# if 0 < quantity < 29:
# candies -= quantity
# print(f'конфет осталось - {candies}')
# else:
# print('Вы ввели некоректное кол-во конфет, введите число от 1 до 28')
# count -=1

# if count % 2 == 0:
# print('победил игрок 2')
# else:
# print('победил игрок 1')

#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# from encodings import utf_8

# with open("words.txt", encoding='utf_8') as fin:
# for line in fin:
# words = line.split()
# for word in words:
# if 'абв' in word:
# words.remove(word)
# sentence = " ".join(words)
# print(sentence)


# Создайте программу для игры в ""Крестики-нолики"".

# doska = list(range(1,10))

# def draw_board(board):

#     for i in range(3):
# print ("|", doska[0+i*3], "|", doska[1+i*3], "|",doska[2+i*3], "|")

# def stavim_hod(hod):
#     valid = False
# while not valid:
#     otvet = input("Введите номер клетки куда поставить значение " + hod+"? ")
# otv = int(otvet)
# if otv >= 1 and otv <= 9:
#     if (str(doska[otv-1]) not in "XO"):
#     doska[otv-1] = hod
# valid = True
# else:
# print ("Эта клетка занята")
# def kto_viigral(doska):
# pobeda = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# for x in pobeda:
#     if doska[x[0]] == doska[x[1]] == doska[x[2]]:
# return doska[x[0]]
# return False

# def igra(doska):
# count = 0
# win = False
# while not win:
# draw_board(doska)
# if count % 2 == 0:
# stavim_hod("X")
# else:
# stavim_hod("O")
# count += 1
# if count > 4:
# m = kto_viigral(doska)
# if m:
# print (m, "Победил!")
# win = True
# break
# if count == 9:
# print ("Победила дружба!")
# break
# draw_board(doska)
