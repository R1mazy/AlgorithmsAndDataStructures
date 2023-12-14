f = open('gogol.txt', 'r', encoding='utf8')
textin = f.read()
lines = textin.splitlines()
txtin = []
for line in lines:
    txtin.append(line)

for i in range(len(txtin)):
    if "салфеткой" in txtin[i]:
        print(txtin[i])


# \copy people from 'D:\homework\AlgorithmsAndDataStructures\hakaton\people.csv' delimiter ',' csv header;

