f = open('gogol.txt', 'r', encoding='utf8')
textin = f.read()
count = textin.count(',')
print(count)