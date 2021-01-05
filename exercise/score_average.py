kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
for sub in midterm_score:
    for i, stu in enumerate(sub):
        student_score[i] += int(stu/3)
else:
    A, B, C, D, E = student_score
    print('average of student is ', student_score)
