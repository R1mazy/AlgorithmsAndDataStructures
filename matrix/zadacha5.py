import random

n, m = input().split()
n = int(n)
m = int(m)

matrix = []
for i in range(n):
        row = [random.randint(0, 100) for j in range(m)]
        matrix.append(row)
print(matrix)

one_matrix = [i for j in matrix for i in j]
print(one_matrix)

for i in range(len(one_matrix)):
    for j in range(len(one_matrix)-i-1):
        if one_matrix[j] < one_matrix[j+1]:
            one_matrix[j], one_matrix[j+1] = one_matrix[j+1], one_matrix[j]

print(one_matrix)

sort_matrix = [[0]*m for i in range(n)]
c = 0

for i in range(n):
         for j in range(m):
                sort_matrix[i][j] = one_matrix[c]
                c += 1

print("Отсортированный массив: ", sort_matrix)