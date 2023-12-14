import json

with open('tme.json') as f:
    data = json.load(f)

element1 = data['from_user']
element2 = element1['username']

print("t.me/" + element2)