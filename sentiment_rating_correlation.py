import pandas as pd
import csv
import numpy as np


df = pd.read_csv('D:/movie_review/new_data_review/confidential assignment/baseline_old/222.csv', sep="abeled", names =['A', 'B'])
count = 1
df['B'] = df['B'].str.replace(',' , '',regex=False)
df['C'] = df.A.str.split(',').str[0]
df['D'] = df.A.str.split(',').str[1]

print(df)
dataframe = pd.DataFrame(df)
dataframe.drop(['A'], axis=1, inplace=True)
dataframe.to_csv("D:/movie_review/new_data_review/confidential assignment/baseline_old/333.csv", encoding="utf-8")


# count = 1
# while (count <= 21267):  # review_data.json 갯수
#
#     labeled1 = True
#     labeled2 = True
#     labeled3 = True
#     line = reading_file.readline()
#     asdf = line.split()
