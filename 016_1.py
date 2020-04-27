from sys import argv
script, filename = argv
print(f"Содержание файла {filename}:")

object = open(filename)
object2 = object.read()
print(object2)
#object.close()

