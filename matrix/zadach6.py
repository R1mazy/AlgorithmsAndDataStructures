n, m = input().split()
n = int(n)
m = int(m)

matrix = [[0] * m for i in range(n)]
k = 1

for summ_i_j in range(1000):
    for i in range(n):
        for j in range(m):
            if i + j == summ_i_j:
                matrix[i][j] = k
                k += 1
for i in matrix:
    print(i)