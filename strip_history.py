from pprint import pprint

count = 1
f = open("D:/movie_review/new_data_review/the_outlaws/baseline_old/1234.txt", "w", encoding='utf-8')
reading_file = open("D:/movie_review/new_data_review/the_outlaws/review_history.txt", "r", encoding='utf-8')
number1 = 0
number2 = 0
number3 = 0
number4 = 0
while (count <= 10000):  # review_data.json 갯수

    line = reading_file.readline()


    f.write(line)
    count += 1