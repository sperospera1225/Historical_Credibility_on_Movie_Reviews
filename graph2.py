import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)
import json
import plotly.graph_objects as go
import pandas as pd
import numpy
import statistics

index = 1
count = 1
rating_list = list()
stedv_list = list()
with open('D:/movie_review/new_data_review/The Spy Gone North/review_data.json',"r",encoding='utf-8') as f:
    review_data = json.load(f)
reading_file = open("D:/movie_review/new_data_review/The Spy Gone North/review_history.txt",  "r",encoding='utf-8')

while(count <= 10):
    line = reading_file.readline()
    asdf = line.split()
    asdf = list(map(int, asdf))
    print(numpy.std(asdf, axis=0))
    stedv_list.append(numpy.std(asdf, axis=0))
    #stedv_list.append(asdf)
    count += 1
while(index <= 10):
    rating = review_data[count - 1]["rating"].strip()
    rating = int(rating)
    print(rating)
    rating_list.append(rating)
    index += 1