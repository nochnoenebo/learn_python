#-*- coding: utf- 8 -*-

from sys import argv 

sсrip, ing1, ing2, ing3, ing4 = argv 

print u"Первый ингредиент:", ing1 
print u"Второй ингредиент:", ing2 
print u"Третий ингредиент:", ing3
print u"Четвертый ингредиент:", ing4
print u"Введите количество блюд:",
sum = int(raw_input())
print u"В ваши %r блюд будет добавлено: %r, %r, %r и %r." % (sum, ing1, ing2, ing3, ing4)