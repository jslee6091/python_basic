import random

guess_number = random.randint(1, 100)
my_guess = int(input())
num = 0

while my_guess != guess_number:
    if my_guess > guess_number:
        print('숫자가 너무 큽니다')
    else:
        print('숫자가 너무 작습니다')
    my_guess = int(input())
    num += 1
else:
    num += 1
    print(f'정답은 {my_guess}이고 당신은 {num}번만에 맞추었습니다.')
