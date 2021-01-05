print('구구단 몇단을 계산할까요?')
num = int(input())

while 1 <= num <= 9:
    print('구구단 ', num, '단을 계산합니다.')
    for i in range(1, 10):
        print(f'{num} * {i} = {num*i}')
    print('구구단 몇단을 계산할까요?')
    num = int(input())
else:
    print(num, '\n구구단 게임을 종료합니다.')
