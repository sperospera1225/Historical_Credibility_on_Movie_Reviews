import json
from pprint import pprint

with open('D:/movie_review/new_data_review/the_outlaws/review_data.json',"r",encoding='utf-8') as f:
    review_data = json.load(f)
count = 1
sum = 0
while(count <= 28531): # review_data.json 갯수
    a=review_data[count-1]["review"]
    b=a.replace("\n관람객\n","")
    c=b.strip()
    d=len(c)
    sum = sum + d
    count += 1

print(sum/28531)