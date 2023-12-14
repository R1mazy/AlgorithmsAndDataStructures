import psycopg2
class connectionDB:
    def __init__(self, user, password, host, port, database):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()
    def select(self):
        self.cursor.execute("select email from people;")
        return self.cursor.fetchall()

c = connectionDB(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'test')


all = c.select()

count = 0
textnew = []
number = []
k = 0

for i in all:
    number = i[0]
    textnew.append(number)
for i in range(len(textnew)):
    for j in textnew[i]:
        if j.isdigit():
            count += 1
    if count != 0:
        k += 1
        count = 0


print(k)
