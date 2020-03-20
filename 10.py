#-*- coding: utf- 8 -*-
d_artagnan = u"\tМеня зовут д'Артаньян."
athos = u"Эта строка\nразделена на 2."
portos = u"Я \\ - \\ мушкетер!"

aramis = u"""
Подсказки:
\t* Граф из Гаскони
\t* Связан с Миледи
\t* Барон\n\t* Генерал Ордена
"""

print d_artagnan
print athos
print portos
print aramis


print u"I need some \"%r.\""  % 'sleep'
print u"You can't go home like \'%r.\'"  % 'this'
print u"I try counting \"%s.\""  % 'sheep'
print u"But there's one i always \'%s.\'"  % 'miss'

while True:
    for i in ["/", "~", "|", "\\", "|"]:
        print " %s\r" %i,