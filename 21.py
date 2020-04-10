def add(a, b):
    print(f"сложение {a} +{b}")
    return a+b

def subtract(a, b):
    print(f"вычитание {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"умножение {a} * {b}")
    return a * b

def divide(a, b):
    print(f"деление {a} / {b}")
    return a / b

print("Давайте выполним несколько вычислений с помощью функций!")

age = add(30, 5)
height = subtract(190, 4)
weight = multiply(30, 2)
iq = divide(250, 2)

print(f"Возраст: {age}, Рост: {height}, Вес: {weight}, IQ: {iq}")

print("Это головоломка.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("Получается: ", what, "Вы можете это вычислить вручную?")
print(age-height+weight*(iq/2)) #проще

flour=divide(100, 2)
egg = multiply(1, 2)
milk = add(1, 1)
print("for pancackes:", add(flour, multiply(milk, egg)))
