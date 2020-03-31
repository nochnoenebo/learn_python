from sys import argv

script, input_file = argv

def print_all(f): #объявление ф-и которая ситает и выводит содержимое файла
    print(f.read())

def rewind(f): #объявление ф-и перемотки в начало файла
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file) #переменная = файлу из аргументов в строке 3

print("Первым делом выведем этот файл целиком:\n")

print_all(current_file) #вывести текст из файла

print("Теперь отмотаем назад, словно это кассета.") #Перемотка в начало файла

rewind(current_file)

print("Выведем три строки:")

current_line = 1 #вывод 1 строки
print_a_line(current_line, current_file)

current_line +=1 #вывод 2 строки
print_a_line(current_line, current_file)

current_line +=1 #вывод 3 строки
print_a_line(current_line, current_file)
