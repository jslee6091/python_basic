# dictionary(dict)
ddd = {}
print(type(ddd), ddd)

ddd[100] = 'what'
ddd[200] = 'the'
ddd[300] = 'hell'
ddd[400] = 234

print(ddd)
print(ddd.get(1009))
if ddd.get(222):
    print('yes dictionary')
else:
    print('no dictionary')

print(100 in ddd)
print('sdk' in ddd)
print('what' in ddd.values())
print(33 in ddd.values())

# zip() function
day = ['monday', 'tuesday', 'wednesday']
fruit = ['apple', 'banana', 'pineapple']
sport = ['football', 'baseball', 'basketball', 'volleyball']
for days, fruits, sports in zip(day, fruit, sport):
    print(days, fruits, sports)

day_tuple = 'monday', 'turea' , 'wedensd'
fruit_tuple = 'fsdf', 'werwe', 'wewewd'
print(type(day_tuple))
print(list(zip(day_tuple, fruit_tuple)))
print(dict(zip(day_tuple, fruit_tuple)))

mixt = [{}, {}, {}, {}]
print(mixt)
