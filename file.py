#1) Чтение файла ---- 'r'
#2) Перезапись файла ----'w'
#3) Добавление файла ----'а'
#4) binary mode ----'b' режим бинарного чтения 
#  прочитать строки --- readlines --- strings = file.readlines()
#  конструкция -  with  --- позволяет мне не писать каждый раз закрытие файла


# 1)Чтение файла ---- 'r'

# filename = input('Укажите файл: ')
# file = open(filename, 'r')
# print('В данном файле '+ str(len(file.read())) + ' символов' )
# file.close()


# 2)Перезапись файла ----'w'

# file = open('file1.txt', 'w')

# file.write('Привет нига')

# file.close()


# Создание нового файла, и текста внутри

# filename = input('Введите желаемое имя файла: ')
# text = input('Какой текст хотите поместить в файл?: ')
# file = open(filename, 'w')
# file.write(text)
# file.close()



# file = open('file1.txt', 'r')

# print(file.read(6))

# ##print(file.read(3))

# file.close()



# 3)Добавление файла ----'а'

# file = open('file1.txt', 'a')

# file.write(' TEST ')

# file.close()



# Программа для копирования файлов!!!

# filename1 = input('Введите название копируемого файла: ')
# filename2 = input('Введите куда скопировать файл: ')

# file1 = open(filename1, "r") #режим чтения
# file2 = open(filename2, "w") #режим перезаписи

# file2.write(file1.read())

# file1.close()
# file2.close()

# print('Копирование успешно завершено!!!')


# --------------------------------------


# filename1 = input('Какой файл забэкапить: ')
# filename2 = 'backup_' + filename1

# file1 = open(filename1, "r") #режим чтения
# file2 = open(filename2, "w") #режим перезаписи

# file2.write(file1.read())

# file1.close()
# file2.close()

# print('Бэкап успешно завершен!!!')





# with open('test.txt', 'wt', encoding='utf-8') as inFile:
# 	inFile.write ("Наш новый файл")

# with open ('test.txt', 'r', encoding='utf-8') as infile:
# 	filename1 = input('Введите название копируемого файла: ')
# 	filename2 = input('Введите куда скопировать файл: ')

# 	file1 = open(filename1, "r") #режим чтения
# 	file2 = open(filename2, "w") #режим перезаписи

# 	file2.write(file1.read())
# 	print('Копирование успешно завершено!!!')




# import os
# os.mkdir("d://test_python1")


# import os
# import glob
# a = input()
# list_papka = []
# list_file = []

# # def get_from_directory(x):
# for elem in glob.glob(a):
# 	if os.path.isfile(elem):
# 		list_file.append(elem)
# 	else:
# 		list_papka.append(elem)
# 		# get_from_directory()

# for elem in glob.glob(a):
# 	if os.path.isdir(elem):
# 		list_papka.append(elem)
# 	else:
# 		list_file.append(elem)

		