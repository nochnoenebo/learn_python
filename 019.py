def cheese_and_crackers(cheese_count, boxes_of_crackers):#передача в ф-ю cheese_and_crackers 2 переменных
    print(f"У нас есть {cheese_count} сырков!")
    print(f"У нас есть {boxes_of_crackers} сырков!")
    print("Этого достаточно для вечеринки!")
    print("Погнали!")

print("Мы можем непосредственно передать числа функции:")
cheese_and_crackers(20, 30) #вызов ф-и со значениями 20 и 30

print("ИЛИ, мы можем использовать переменные из нашего сценария:")
amount_of_cheese =10 # переменной задаем значение
amount_of_crackers = 50

cheese_and_crackers(10+20, 5+6) # вызов ф-и с вычислениями

print("И объединить переменные с вычислениями:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #вызов ф-и с вычислениями включающими переменные

