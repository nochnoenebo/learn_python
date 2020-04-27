from sys import argv
#берем 2 значения из командной строки
script, filename = argv
#переменная txt считывает содержимое Filename
txt = open(filename, 'r')
#вывод в строке названия файла
print(f"Содержимое файла {filename}:")
print(txt.read()) #вывод переменной txt
print("Снова введите имя файла:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
