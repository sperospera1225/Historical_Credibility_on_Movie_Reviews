
with open("D:/movie_review/new_data_review/amsal/baseline_old/trusted_positive_sympathy.txt",'r',encoding='UTF8') as f:
    list_file = []
    for line in f:
        list_file.append(line)

with open("D:/movie_review/new_data_review/amsal/baseline_old/review_history_trusted_comment_noempty.txt",'r', encoding='UTF8') as f2:
    list_file2 = []
    for line in f2:
        list_file2.append(line)

list_file3 = list_file + list_file2
my_set = set(list_file3)
list_file4 = list(my_set)

print(len(list_file4))


