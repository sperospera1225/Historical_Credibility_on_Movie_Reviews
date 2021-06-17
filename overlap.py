
with open("D:/movie_review/new_data_review/1987/baseline_old/review_history_helpful.txt",'r',encoding='UTF8') as f:
    list_file = []
    for line in f:
        list_file.append(line.replace('\n',''))

with open("D:/movie_review/new_data_review/1987/baseline_old/trusted2.txt",'r', encoding='UTF8') as f2:
    list_file2 = []
    for line in f2:
        list_file2.append(line.replace('\n',''))


print(len(list_file))
print(len(list_file2))

list_file3 = list_file + list_file2
print(len(list_file3))
my_set = set(list_file3)
list_file4 = list(my_set)


print(len(list_file4))
print(len(list_file3)-len(list_file4))


