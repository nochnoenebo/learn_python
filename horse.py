import random
from random import randint
a = randint(0, 7)
b = randint(0, 7)
print(a, b)
m = 8
n = 8
matrix = [[0 for b in range(m)] for a in range(n)]
if a in range(m):
    for f in range(n):
        matrix[a][b] = 1
    print(matrix)


i, j = (int(i) for i in input().split())
# if 0 <= i <= 7 and 0 <= j <= 7:
#     matrix = [[0 for j in range(m)] for i in range(n)]
#     if i in range(m):
#         for f in range(n):
#             matrix[i][j]= 1
#         print(matrix)
# else:
#     print("fuck this shit.")
if (abs(a - i) == 2 and abs(b - j) == 1) or (abs(a - i) == 1 and abs(b - j) == 2):
    print ("horse")
    matrix = [[0 for j in range(m)] for i in range(n)]
    if i in range(m):
        for f in range(n):
            matrix[i][j] = 1
        print(matrix)
else:
    print ("not_horse")
