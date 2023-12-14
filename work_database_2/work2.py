import psycopg2
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from datetime import datetime
from operator import itemgetter
from scipy import interpolate
from scipy.interpolate import make_interp_spline, BSpline

# 433100526928004

class connectionDB:
    def __init__(self, user, password, host, port, database):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()
    def select(self):
        self.cursor.execute("select messages.timestamp, messages.can_data from messages where terminal_id = '433100526928004' limit 100;")
        return self.cursor.fetchall()

class connectionDBnew:
    def __init__(self, user, password, host, port, database):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()
    def select(self):
        self.cursor.execute("select calibrating.calibrating_data from calibrating where deviceid_port = '433100526928004_4' limit 100;")
        return self.cursor.fetchall()

c = connectionDB(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'test')

d = connectionDBnew(user='Lebedev', password = 'root', host = 'localhost', port = '5433', database = 'test')


all = c.select()
print(all)
[all2] = d.select()
all2 = all2[0]
print('CALIB', all2)

calib_data_in = []
calib_data_out = []

for i in all2:
    calib_data_in.append(i['input_value'])
    calib_data_out.append(i['output_value'])

f = interpolate.interp1d(calib_data_in, calib_data_out)


y = []
x = []
fuel = []
data_times = []

avg = []
for i in all:
    avg.append(i[1])
for i in all:
    data_times.append(i[0])
# for i in all:
#     # data_times.append(datetime.utcfromtimestamp(i[0]).strftime('%Y-%m-%d %H:%M:%S'))
#     data_times.append(datetime)
print(data_times)
for i in avg:
    fuel.append(f(i['LLS_0']))
print(fuel)

for i in range(len(data_times)-1):
    for j in range(len(data_times)-i-1):
        if data_times[j] > data_times[j+1]:
            data_times[j], data_times[j+1] = data_times[j+1], data_times[j]
            fuel[j], fuel[j + 1] = fuel[j + 1], fuel[j]


timest = list(set(data_times))
x = np.array(data_times)
y = np.array(fuel)

xnew = np.linspace(x.min(), x.max(), 200)

spl = make_interp_spline(x, y, k=3)
y_smooth = spl(xnew)

plt.plot(xnew, y_smooth)
plt.show()































# cursor = conn.cursor()
#
# cursor.execute(
#     "SELECT timestamp, can_data FROM messages WHERE terminal_id = '433100526928004' LIMIT 500;")
#
# data = cursor.fetchall()
#
# cursor.execute(
#     "SELECT calibrating_data FROM calibrating WHERE deviceid_port = '433100526928004_4';")
#
# [calibrating_data] = cursor.fetchall()
# calibrating_data = calibrating_data[0]
#
# calibrating_data_input = []
# calibrating_data_output = []
#
# for inputs in calibrating_data:
#     calibrating_data_input.append(inputs['input_value'])
#     calibrating_data_output.append(inputs['output_value'])
#
# f = interpolate.interp1d(calibrating_data_input, calibrating_data_output)
# t = []
# cd = []
# t_stamp = []
#
# for time, can_data in data:
#     if time not in t_stamp:
#         t_stamp.append(time)
#         tm = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
#         t.append(tm)
#         cd.append(f(can_data['LLS_0']))
#
# for k in range(len(t) - 1):
#     for j in range(len(t) - 1):
#         if t[j] > t[j + 1]:
#             t[j + 1], t[j] = t[j], t[j + 1]
#             cd[j + 1], cd[j] = cd[j], cd[j + 1]
#         if t_stamp[j] > t_stamp[j + 1]:
#             t_stamp[j + 1], t_stamp[j] = t_stamp[j], t_stamp[j + 1]
#
# x = np.array(t_stamp)
# y = np.array(cd)
#
# xnew = np.linspace(x.min(), x.max(), 200)
#
# spl = make_interp_spline(x, y, k=3)
# y_smooth = spl(xnew)
#
# plt.plot(xnew, y_smooth)
#
# plt.show
# ()