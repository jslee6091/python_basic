print(range(10))
for i in range(2, 20, 2):
    print(i)

wish_travel_cities = {
    'japan': 'tokyo',
    'korea': 'seoul',
    'usa': 'washington',
    'china': 'beijing'
}
print(wish_travel_cities.items())
print(wish_travel_cities['japan'])

for key in wish_travel_cities.keys():
    print(f'I want to visit {wish_travel_cities[key]} of {key}')

print('-------------')
for k, v in wish_travel_cities.items():
    print(f'I want to visit {v} of {k}')

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("error")