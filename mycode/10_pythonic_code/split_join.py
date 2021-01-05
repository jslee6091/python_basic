my_str = 'java python kotlin'
my_list = my_str.split()
print(type(my_list), my_list)

my_str2 = ''.join(my_list)
print(my_str2)

my_str3 = 'java,python,kotlin'
my_list2 = my_str3.split(',')
print(type(my_list2), my_list2)
my_str4 = '/'.join(my_list2)
print(my_str4)

# for + append
result = []
for i in range(10):
    result.append(i)
print(result)

result2 = [i for i in range(10)]
print(result2)

my_str4 = "Hello"
my_str5 = "World"
result3 = [i + j for i in my_str4 for j in my_str5]
print(result3)

words = 'Arguments can be passed to functions in four different ways'.split()
print(words)

for w, t in enumerate(words):
    print(w, t)

print(list(enumerate(words)))
word_dict = {w: x for w, x in enumerate(words, 1)}
print(word_dict)

my_zip = [1, 2, 3]
my_zip2 = [10, 20, 30]
my_zip3 = [100, 200, 300]
print(list(zip(my_zip, my_zip2, my_zip3)), type(list(zip(my_zip, my_zip2, my_zip3))))

result4 = [sum(val) for val in zip(my_zip, my_zip2, my_zip3)]
print(result4)

result_dict = {idx: sum(val) for idx, val in enumerate(zip(my_zip, my_zip2, my_zip3))}
print(result_dict)

a, b, c = zip(my_zip, my_zip2, my_zip3)
print(a, b, c)
