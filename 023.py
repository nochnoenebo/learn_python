import sys
script, encoding, error = sys.argv # обработка аргумента командной строки
# .encode() - закодировать строку
# .decode() - декодировать

def main(language_file, encoding,  errors):
    line = language_file.readline() # считать одну строку из файла

    if line: # если есть строка
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # вызов функции внутри нее самой для цикла

def print_line(line, encoding, errors): #кодирование
    next_lang = line.strip() # удаление /n в конце строки line?
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)
