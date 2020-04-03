import random
from random import randint
i = randint(0, 7)
j = randint(0, 7)
print (i, j)
m = 8
n = 8
matrix = [[0 for j in range(m)] for i in range(n)]
if i in range(m):
    for f in range(n):
        matrix[i][j]= 1
    print (matrix)


i, j = (int(i) for i in input().split())
#print (i, j)
if 0<=i<=7 and 0<=j<=7:
    matrix = [[0 for j in range(m)] for i in range(n)]
    if i in range(m):
        for f in range(n):
            matrix[i][j]= 1
        print (matrix)
else:
    print ("fuck this shit.")
