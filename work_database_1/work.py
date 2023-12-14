import psycopg2
from random import randint
import matplotlib.pyplot as plt
from datetime import datetime
from operator import itemgetter

class connectionDB:
    def __init__(self, user, password, host, port, database):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()
    def select(self):
        self.cursor.execute("select messages.timestamp, messages.can_data from messages where terminal_id = '433100526928099' limit 10;")
        return self.cursor.fetchall()

c = connectionDB(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'test')


all = c.select()
print(all)

# for i in all:
#     for j in range(len(all)):
#         print(i[j])
y = []
x = []
f = []
#
# for i in all:
#     print(i[1])
avg = []
for i in all:
    avg.append(i[1])
for i in all:
    x.append(datetime.utcfromtimestamp(i[0]).strftime('%Y-%m-%d %H:%M:%S'))
print(x)
for i in avg:
    if i['LLS_0']:
        f.append(i['LLS_0'])
print(f)


# result = list(map(itemgetter(0), all))
# result1 = list(map(itemgetter(0), result))
# print(result)
# for i in result:
#     x.append(i[0])
#     y.append(i[1])
#     print(i)
# x = [i[0] for i in result]
# y = [i[1] for i in result]
# print(y)
#
# for i in range(len(y)):
#     print("Время превышение скорости: ", x[i], ". Превышена скорость на: ", int(y[i]) - 40)

# plt.plot(x, y)
# plt.show()

