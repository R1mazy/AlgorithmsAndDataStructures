import random

n, m = input().split()
n = int(n)
m = int(m)

matrix = []
for i in range(n):
        row = [random.randint(0, 100) for j in range(m)]
        matrix.append(row)
max = -5

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]
print(matrix)
print("Максимальное число в матрице ", max)
