f = open('gogol.txt', 'r', encoding='utf8')
textin = f.read()
lines = textin.replace('\n', ' ')
txtin = lines.split()
count = 0

for i in range(len(txtin)):
    if "совершенно" in txtin[i]:
        count = i
print(count)