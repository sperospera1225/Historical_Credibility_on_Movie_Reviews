
from eunjeon import Mecab 
import json
from pprint import  pprint
import os


dir_folder = os.path.dirname(os.getcwd()).replace("\\", "/")

dir_file_r = dir_folder + "/movie_review/new_data_review/amsal/baseline_old"
dir_file_w = dir_folder + "/movie_review/rearrangement/amsal"

cate_1 = dir_file_w + "/category__external_beauty.txt"
cate_2 = dir_file_w + "/category__casts_staffs.txt"
cate_3 = dir_file_w + "/category__massages_subjects.txt"
cate_4 = dir_file_w + "/category__etc.txt"
countReview = [0, 0, 0, 0]
category = [[], [], [], []]
c1 = open(cate_1, 'r')
c2 = open(cate_2, 'r')
c3 = open(cate_3, 'r')
c4 = open(cate_4, 'r')
container = [c1, c2, c3, c4]
for i in range(len(container)):
    for j in container[i]:
        j = j.replace("\n", "")
        category[i].append(j)

if not os.path.exists(dir_file_w):
    os.makedirs(dir_file_w)

read_1 = dir_file_r + "/review_history_trusted_comment_noempty.txt"
read_2 = dir_file_r + "/review_history_untrusted_comment_noempty.txt"
rawData = [open(read_1, 'r', encoding='utf-8'), open(read_2, 'r',encoding='utf-8')]

write_1 = dir_file_w + "/external_beauty.txt"
write_2 = dir_file_w + "/casts_staffs.txt"
write_3 = dir_file_w + "/massages_subjects.txt"
write_4 = dir_file_w + "/etc.txt"
writeData = [open(write_1, 'w+t', encoding='utf-8'), open(write_2, 'w+t', encoding='utf-8'), open(write_3, 'w+t', encoding='utf-8'), open(write_4, 'w+t', encoding='utf-8')]

mecab = Mecab()

for file in rawData:
    for line in file:
        counter = []
        yCheck = [0, 0, 0, 0]
        for i in mecab.nouns(line):
            counter.append(i)
        for i in range(len(category)):
            for j in counter:
                if j in category[i]:
                    yCheck[i] = 1
        for i in range(len(yCheck)):
            if yCheck[i] == 1:
                writeData[i].write(line)
                countReview[i] += 1
print(countReview)
