from test import connectionDB
import matplotlib.pyplot as plt

c = connectionDB(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'planes')

all = c.select()
print(all)
x = [i[0] for i in all]
y = [i[1] for i in all]

x1 = x
x2 = x

y1 = y
y2 = y


for i in range(len(x1)-1):
    for j in range(len(x1)-i-1):
        if x1[j] > x1[j+1]:
            x1[j], x1[j+1] = x1[j+1], x1[j]
print(x1)

for i in range(len(y1)-1):
    for j in range(len(y1)-i-1):
        if y1[j] > y1[j+1]:
            y1[j], y1[j+1] = y1[j+1], y1[j]
print(y1)

plt.plot(x1, y1)
plt.show()

for i in range(len(x2)-1):
    for j in range(len(x2)-i-1):
        if x2[j] < x2[j+1]:
            x2[j], x2[j+1] = x2[j+1], x2[j]
print(x2)

for i in range(len(y2)-1):
    for j in range(len(y2)-i-1):
        if y2[j] < y2[j+1]:
            y2[j], y2[j+1] = y2[j+1], y2[j]
print(y2)

plt.plot(x2, y2)
plt.show()