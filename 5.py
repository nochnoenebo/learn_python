#-*- coding: utf- 8 -*-
name = u'Зед Шоу'
age = 35 # это правда!
height = 188 #см
weight = 80.5 #кг
eyes = u'Голубые'
teeth = u'Белые'
hair = u'Каштановые'

print u"Давайте поговорим о человеке по имени %s." %name
print u"Его рост составляет %d см." %height
print u"Он весит %d кг." %weight

print u"На самом деле это не так и много."
print u"У него %s глаза и %s волосы." %(eyes, hair)
print u"Его зубы обычно %s, хотя он и любит кофе." %teeth

#эта строка кода доволно сложная, не ошибитесь!
print u"Если я сложу %d, %d и %d, то получу %d." %(age, height, weight, age + height + weight)
print u"Его зубы обычно %r, хотя он и любит кофе." %teeth
print u"Он весит %r кг." %weight

sm = 45
kg = 15

print u"%d см = %g дюймов" %(sm, sm*0.393701)
print u"%d км = %g фунтов" %(kg, kg*2.20462)