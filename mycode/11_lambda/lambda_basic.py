def add(x, y):
    return x + y


print(add(2, 4))

add2 = lambda x, y: x + y
print(add2(3, 4))
print((lambda x, y: x + y)(5, 7))
print((lambda x: x ** 2)(8))

double_val = lambda x: x ** 2
my_list = [1, 2, 3, 4, 5]
result = map(double_val, my_list)
print(list(result), type(result))

double_even = lambda x: x ** 2 if x % 2 == 0 else x
print(double_even(4), double_even(5))
print(list(map(double_even, my_list)))
print(type(map(double_even, my_list)))

from functools import reduce

add3 = lambda x, y: x + y
result2 = reduce(add3, my_list)
print(result2)

result3 = reduce(add3, ['i', 'love', 'you'])
print(result3)

my_filter = lambda my_str: len(my_str) > 5
my_str = ['hew', 'wedhy', 'ikoljujh', 'gj', 'eyjnvx']
result4 = filter(my_filter, my_str)
print(type(result4), list(result4))
