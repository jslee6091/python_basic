books = list()
books.append({'제목': '개발자의 코드', '출판연도': '2013.02.28', '출판사': 'A출판', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B출판 ', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A출판 ', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B출판 ', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'C출판 ', '쪽수': 248, '추천유무': True})

my_page_list = list()
recommand_list = list()
publisher_list = set()

for i in books:
    print(i['쪽수'])
    if i['쪽수'] > 250:
        my_page_list.append(i['제목'])
    if i['추천유무']:
        recommand_list.append(i['제목'])
    publisher_list.add(i['출판사'].strip())

print('250쪽 넘는 책 :', my_page_list)
print('추천유무 true :', recommand_list)
print('출판사 목록 :', publisher_list)

my_page_list2 = [j['제목'] for j in books if j['쪽수'] > 250]
recommand_list2 = [j['제목'] for j in books if j['추천유무']]
publisher_list2 = set([j['출판사'].strip() for j in books])
print(my_page_list2)
print(recommand_list2)
print(publisher_list2)
