from work import connectionDB
import matplotlib.pyplot as plt

c = connectionDB(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'test')

all = c.select()
print(all)
