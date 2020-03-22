#-*- coding: utf- 8 -*-

import codecs, sys
outf = codecs.getwriter('cp866')(sys.stdout, errors='replase')
sys.stdout = outf

age = raw_input(u"Сколько тебе лет?")
height = raw_input(u"Какой твой рост?")
weight = raw_input(u"Сколько ты весишь?")

print u"Итак, тебе %r лет, в тебе %r см роста и %r кг веса." % (age, height, weight)