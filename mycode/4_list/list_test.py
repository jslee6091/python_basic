num = [2, 3, 4, 5, 6]
print(type(num), num)
print(num[0], num[:3])
for val in num:
    print(val)

for index, arr in enumerate(num):
    print(index, arr)

str_list = ['dsf', 'wer', 'werwd', 'oiel', 'wq']
str_list[1] = 'javascript'
str_list.insert(2, 'woww')
print(type(str_list), str_list)
print(str_list[3], str_list[:2])
print(str_list * 2)
print('dsf' in str_list)

for ind, arr in enumerate(str_list):
    print(ind, arr)

mix_list = [32, 'hew', 4.6]
mix_list.append('what')
for mmm in mix_list:
    print(type(mmm), mmm)

print(str_list == mix_list)