n = 5
matrix = []


for i in range(1, n+1):
    a = []
    if i % 2 == 1:
        a = list(range(1, n+1))
    else:
        a = [i] * n
    matrix.append(a)
print(matrix)





