import psycopg2
class connectionDB:
    def __init__(self, user, password, host, port, database):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()
    def select(self):
        self.cursor.execute("select phone_number from people;")
        return self.cursor.fetchall()

c = connectionDB(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'test')


all = c.select()

count = ""
textnew = []
number = []
k = 0

for i in all:
    number = i[0]
    textnew.append(number)
for i in range(len(textnew)):
    count = textnew[i]
    if count[:2] == "+7":
        k += 1


print(k)
