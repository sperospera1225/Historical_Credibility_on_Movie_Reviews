

f1 = open("D:/movie_review/new_data_review/the_outlaws/baseline_old/t_0_10_sympathy_3.txt",  "r", encoding='utf-8')
f2 = open("D:/movie_review/new_data_review/the_outlaws/baseline_old/1_10_tt.txt",  "w", encoding='utf-8')
# with codecs.open(filename1, 'r', 'utf-8') as f7:
lines1 = f1.readlines()

# lines1 = lines1.split(",")[1]
# print(lines1)

for line in lines1:
    line2 = line.split(",")[0]
    f2.write(line2)
    f2.write('\n')
    # print(line2)
    # print(line.split(",")[3].replace('\n',''))
    # if line.split(",")[3].replace('\n','') == 'l':
    #     print('1111111111111111111111111111111')