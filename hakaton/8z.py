import psycopg2
class connectionDB:
    def __init__(self, user, password, host, port, database):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()
    def select(self):
        self.cursor.execute("select name, date_of_birth, address from people;")
        return self.cursor.fetchall()

c = connectionDB(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'test')


all = c.select()

count = ""
textnew1 = []
textnew2 = []
textnew3 = []
number = []
k = 0

for i in all:
    number = i[0]
    textnew1.append(number)
    number = i[1]
    textnew2.append(number)
    number = (i[2]).replace('\n', ' ')
    textnew3.append(number)


textinp = input()

for i in range(len(textnew1)):
    if textnew1[i] == textinp or textnew2[i] == textinp or textnew3[i] == textinp:
        print("Имя: ", textnew1[i], "   Год рождения: ", textnew2[i], "  Город: ", textnew3[i])

