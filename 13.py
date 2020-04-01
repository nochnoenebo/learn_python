from sys import argv

sсrip, ing1, ing2, ing3, ing4 = argv 

print ("Первый ингредиент:", ing1)
print ("Второй ингредиент:", ing2)
print ("Третий ингредиент:", ing3)
print ("Четвертый ингредиент:", ing4)
print ("Введите количество блюд:"),
sum = int(input())
print ("В ваши %d блюд будет добавлено: %s, %s, %s и %s." % (sum, ing1, ing2, ing3, ing4))
