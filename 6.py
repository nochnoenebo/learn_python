#объявляем переменную x c подстановкой в строку числа, поэтому %d
x = "Существует %d типов людей." %10
#тут u не нужна, т.к. Eng
binary = "Python"
do_not = "нет"
# объявляем переменную y = строке с подстановкой в строку объявленных выше переменных
y = ("Те, кто понимает %r, и те, кто - %s." %(binary, do_not))
# выводим значения переменных
print (x)
print (y)
# выводим строки с подстановкой в них переменных
print ("Я сказал: %s." % x)
print ("А еще я сказал: ' %s'/" %y)
# присваиваем переменной hilarious значение False
hilarious = False
# присваиваем переменной joke_evaluation строку с подстановкой
joke_evaluation = ("Разве это не смешно?! %r")
# выводим joke_evaluation со вставкой в строку переменной hilarious
print (joke_evaluation % hilarious)
# объявим 2 переменные = строкам
w = "Это часть строки слева..."
e = " а это справа."
# вывод строки складывающейся из 2-х переменных объявленных выше
print (w + e)