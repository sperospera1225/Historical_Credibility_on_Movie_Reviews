# 1: 영상미+음악 | 2: 배우+감독 | 3: 주제+메세지 | 4. 기타 | 5. 버림

import os

dir_folder = os.path.dirname(os.getcwd()).replace("\\", "/")

dir_dictionary = dir_folder + "/movie_review/rearrangement/amsal/noun_numbered.txt"
dictionary = open(dir_dictionary, 'r')

dic = []
dicnum = []
for line in dictionary:
    temp = [line[1:], int(line[0:1])]
    dic.append(temp[0])
    dicnum.append(temp[1])



dir_file_r = dir_folder + "/movie_review/rearrangement/amsal/noun.txt"
dir_file_w = dir_folder + "/movie_review/rearrangement/amsal"

write_1 = dir_file_w + "/category__external_beauty.txt"
write_2 = dir_file_w + "/category__casts_staffs.txt"
write_3 = dir_file_w + "/category__massages_subjects.txt"
write_4 = dir_file_w + "/category__etc.txt"
w1 = open(write_1, 'w+t')
w2 = open(write_2, 'w+t')
w3 = open(write_3, 'w+t')
w4 = open(write_4, 'w+t')
w = [w1, w2, w3, w4]
cate = [[], [], [], []]

original = open(dir_file_r , 'r')


for line in original:
    if dicnum[dic.index(line)] != 5:
        print(dic.index(line))
        print(dicnum[0])
        cate[dicnum[dic.index(line)] - 1].append(line) # 3이면 2번째 배열에 넣는다

for i in range(len(cate)):
    for j in cate[i]:
        w[i].write(str(j))