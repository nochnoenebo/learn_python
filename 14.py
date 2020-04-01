from sys import argv
script, user_name = argv
prompt = 'your_answer: '

print ("Привет %s, Я — сценарий %r." % (user_name, script))
print ("Я хочу задать тебе несколько вопросов.")
print ("Я тебе нравлюсь, %s?" % user_name)
likes = input(prompt)

print ("Тде ты живешь, %s?" % user_name)
lives = input(prompt)


print ("Чем ты занимаешься, %s?" % user_name)
doing = input(prompt)

print ("%s, ты позовешь меня на свидание?" % user_name)
date = input(prompt)

print ("""
Итак, ты ответил %r на вопрос, нравлюсь ли я тебе.
Ты живешь в %r. Чудесно.
Ты занимаешься %r. Любопытно!
Наверное я тоже %r.
""" % (likes, lives, doing, date))
