one = {'id': '1', 'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-2343-9870'}
two = {'id': '2', 'name': 'lee soonsin', 'email': 'lee@mail.com', 'hp_num': '010-3333-5555'}
three = {'id': '3', 'name': 'jang youngsil', 'email': 'jang@mail.com', 'hp_num': '010-7777-1234'}
four = {'id': '4', 'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-4567-0987'}

total_list = [one, two, three, four]

for idx, dicts in enumerate(total_list):
    print(idx+1, '번째 keys : ', dicts.keys(), ', values : ', dicts.values())
