import random
from random import randint
a = randint(0, 7)
b = randint(0, 7)
print(a, b)
m = 8
n = 8

""" # вывод доски с пронумерованными строкой и столбцом
for i in range (0, 8):
    print ('\t',i, end='')
print()
for i in range(0, 8):
    print (i, end='')
    for j in range(0, 8):
        print('\t',0, end='')
    print()
"""
matrix = [[0 for b in range(m)] for a in range(n)]
matrix[a][b] = 1
for i in range(m):
    print(*matrix[i])

i, j = (int(i) for i in input().split())
while (i>7 or i<0 or j>7 or j<0) or not ((abs(a - i) == 2 and abs(b - j) == 1) or (abs(a - i) == 1 and abs(b - j) == 2)):
    print("недопустимые координаты")
    i, j = (int(i) for i in input().split())
matrix = [[0 for j in range(m)] for i in range(n)]
matrix[i][j] = 1
for i in range(m):
    print(*matrix[i])
