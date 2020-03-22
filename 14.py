#-*- coding: utf- 8 -*-

import codecs, sys
outf = codecs.getwriter('cp866')(sys.stdout, errors='replace')
sys.stdout = outf

from sys import argv
script, user_name = argv
prompt = 'your_answer: '

print u"Привет %s, Я — сценарий %r." % (user_name, script)
print u"Я хочу задать тебе несколько вопросов."
print u"Я тебе нравлюсь, %s?" % user_name
likes = raw_input(prompt).decode(sys.stdin.encoding or
locale.getpreferredencoding(True))

print u"Тде ты живешь, %s?" % user_name
lives = raw_input(prompt).decode(sys.stdin.encoding or
locale.getpreferredencoding(True))


print u"Чем ты занимаешься, %s?" % user_name
doing = raw_input(prompt).decode(sys.stdin.encoding or
locale.getpreferredencoding(True))

print u"%s, ты позовешь меня на свидание?" % user_name
date = raw_input(prompt).decode(sys.stdin.encoding or
locale.getpreferredencoding(True)) 

print u"""
Итак, ты ответил %r на вопрос, нравлюсь ли я тебе.
Ты живешь в %r. Чудесно.
Ты занимаешься %r. Любопытно!
Наверное я тоже %r.
""" % (likes, lives, doing, date)