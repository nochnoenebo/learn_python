import random
from random import randint
i = randint(0, 7)
j = randint(0, 7)
print(i, j)

matrix = [[0 for j in range(8)] for i in range(8)] #матрица
matrix[i][j]=1
print(matrix)



def coord():
    (int(i) for i in input().split())
x, y = coord()

while x>7 or y>7:
    print("что-то больше 7")
    x, y = coord()
if [x][y]==[i-1][j+2] or [x][y]==[i+1][j+2] or [x][y]==[i+2][j+1] or [x][y]==[i-2][j+1] or [x][y]==[i+2][j-1] or [x][y]==[i-2][j-1] or [x][y]==[i-1][j-2] or [x][y]==[i+1][j-2]:

    matrix = [[0 for y in range(8)] for x in range(8)]
    matrix[x][y] = 1
else:
    coord()

#matrix = [[0 for j in range(m)] for i in range(m)]
#matrix[i][j]=1
print(matrix)
