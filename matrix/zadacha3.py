import random

n, m = input().split()
n = int(n)
m = int(m)

matrix = []
for i in range(n):
        row = [random.randint(0, 100) for j in range(m)]
        matrix.append(row)
min = 150

for i in range(n):
    for j in range(m):
        if matrix[i][j] < min:
            min = matrix[i][j]
print(matrix)
print("Минимальное число в матрице ", min)