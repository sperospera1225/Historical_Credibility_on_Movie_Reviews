import json
from pprint import pprint
count = 1
reading_file = open("D:/movie_review/new_data_review/amsal/review_history.txt",  "r",encoding='utf-8')
number1=0

while(count <= 39521): # review_data.json 갯수
    labeled1 = True
    labeled2 = True
    line = reading_file.readline()
    asdf = line.split()
    asdf = list(map(int, asdf))
    asdf = list(set(asdf))
    number1 = number1 + len(asdf)
    count += 1

print(number1/39521)