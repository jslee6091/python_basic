greet = 'hello' * 4 + ' people' + '\n'
end = 'gogogo'
en2 = 'my name is \'jae sung lee\' thank you'
print(greet + end + '\n' + en2)

# string offset (or index)
value1 = 'hello world'
print('string length is', len(value1))
print('format : string length is {} and first index is {}'.format(len(value1),value1[10]))
# after 3.6 version
print(f'format : string length is {len(value1)}')

# slicing -> [start:end:step] (default value of step is 1 and can omit)
print('from 0 to 5 are ', value1[0:5])
print('from 6 to 11 are ', value1[6:11])
print('before 5 are ', value1[:5])
print('after 6 are ', value1[6:])
print('all are ', value1[:])
print('2칸씩 출력 ', value1[::2])
print('minus index is', value1[-1:])
print('minus index is', value1[-3:])
print('reverse string', value1[::-1])

# string functions
word = 'gooDManUfactuRingpraCtIcegOod'
print('\n' + word)
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.title())
print(word.find('o'))
print(word.rfind('o'))
print(word.startswith('fac'))
print(word.startswith('goo'))
print(word.count('an'))
print(word.split())
print(word.split('tuR'))
print(word.islower())
print(word.isupper())
word2 = 'ERIDF'
word3 = 'sfdfd'
print(word2.islower())
print(word2.isupper())
print(word3.islower())
print(word3.isupper())
for val in word:
    print(val, word.count(val))