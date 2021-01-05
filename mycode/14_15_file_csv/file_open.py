with open('i_have_a_dream.txt', 'r') as my_file:
    contents = my_file.read()
    # 공백을 기준으로 단어 분리
    word_list = contents.split(" ")
    # 한 줄 씩 분리해서 리스트로 저장
    line_lsit = contents.split("\n")

print(f'Total number of characters {len(contents)}')
print(f'Total number of words {len(word_list)}')
print(f'Total number of lines {len(line_lsit)}')
