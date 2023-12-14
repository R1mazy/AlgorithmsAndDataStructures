import psycopg2
from random import randint
import matplotlib.pyplot as plt

class connectionDB:
    def __init__(self, user, password, host, port, database):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()
    def select(self):
        #self.cursor.execute("CREATE TABLE plane(name text, input text, output text);")
        #self.connection.commit()
        # for i in range(10):
        #     self.cursor.execute("insert into plane values (%s, %s, %s);", (str(input()), str(input()), str(input())))
        #     self.connection.commit()
        # self.cursor.execute("select * from plane where name = 'АЭРОФЛОТ';")
        # self.cursor.execute("select * from plane where name != 'АЭРОФЛОТ';")
        # self.cursor.execute("delete from plane where name = 'АЭРОФЛОТ';")
        # self.connection.commit()
        # self.cursor.execute("delete from plane where name = 'S7';")
        # self.connection.commit()
        # self.cursor.execute("update plane set name='АЭРОЛОТ2' where name = 'АЭРОФЛОТ';")
        # self.connection.commit()
        # self.cursor.execute("delete from plane where name = 'S7';")
        # self.connection.commit()
        # self.cursor.execute("CREATE TABLE number(x integer, y integer);")
        # self.connection.commit()
        # for i in range(30):
        #     self.cursor.execute("insert into number (x, y) values(%s, %s);", (randint(0, 10), randint(0, 10)))
        #     self.connection.commit()
        self.cursor.execute("select * from number;")
        return self.cursor.fetchall()

c = connectionDB(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'planes')

print(c.select())

# all = c.select()
# print(all)
# x = [i[0] for i in all]
# y = [i[1] for i in all]
#
# plt.plot(x, y)
# plt.show()