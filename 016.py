from sys import argv

script,filename = argv #берем 2 значения из командн.строки

print(f"Я собираюсь стереть файл {filename}.") #f - чтение названия filename
print("Если вы не хотите его стирать, нажмите сочетание клавишь CTRL+C (^C).")
print("Если хотите стереть файл, нажмите клавишу Enter.")

input("?")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла. До свидания!")
target.truncate() #усечение размера файла

print("Теперь я запрашиваю у вас три строки")

line1 = input("строка 1: ") # переменная принимает введенное значение
line2 = input("строка 2: ")
line3 = input("строка 3: ")

print("Это я запишу в файл.")

target.write(line1) #запись в файл значения переменной
target.write("\n") #переход на следующую строку
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("И, наконец, я закрою файл.")
target.close() #закрытие файла
