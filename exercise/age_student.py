# age = now year - born year +1
from datetime import datetime as dt

current = dt.today().year
print(current)

my_year = int(input())
print(type(my_year))
age = current - my_year + 1

if 17 <= age < 20:
    print('you are high school student!')
elif 20 <= age <= 27:
    print('you are university student!')
else:
    print('you are not student!')
