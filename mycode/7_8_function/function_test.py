def average(num):
    total = 0
    for nn in num:
        total += nn
    avg = total / len(num)
    return int(avg)


def main():
    my_list = [3, 5, 7, 32, 41]
    ans = average(my_list)
    print('average number is ', ans)


def connect(server, port):
    url = f'http://{server}:{port}'
    return url


main()
print(connect('localhost', 8080))
print(connect(port='80', server='aa.com'))
print(connect('naver.com', port=87))


def add(a=20, b=10):
    return a + b


print(add(33, 44))
print(add())
print(add(22))
print(add(b=33))


def add2(a, b, *p):
    print(type(p))
    print(a, b, p)
    return a + b + sum(p)


def add3(**p):
    print(p, type(p))
    for i, j in p.items():
        print(i, j)


print(add2(3, 5, 6, 7))
add3(a=100, b=200, c=300)


def swap(a, b):
    return b, a


result = swap(10, 20)
print(result, type(result))

x, y = swap(20, 30)
print(f'x is {x} and y is {y}')
