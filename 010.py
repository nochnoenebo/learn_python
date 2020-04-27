d_artagnan = ("\tМеня зовут д'Артаньян.")
athos = ("Эта строка\nразделена на 2.")
portos = ("Я \\ - \\ мушкетер!")

aramis = """
Подсказки:
\t* Граф из Гаскони
\t* Связан с Миледи
\t* Барон\n\t* Генерал Ордена
"""

print (d_artagnan)
print (athos)
print (portos)
print (aramis)


print ("I need some \"%r.\""  % 'sleep')
print ("You can't go home like \'%r.\'"  % 'this')
print ("I try counting \"%s.\""  % 'sheep')
print ("But there's one i always \'%s.\'"  % 'miss')

while True:
    for i in ["/", "~", "|", "\\", "|"]:
        print (" %s\r" %i,)