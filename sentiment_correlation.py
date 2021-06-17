import pandas as pd
import csv
import numpy as np

f = open('D:/333.csv','r',encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    print(line)
f.close()
#
# df = pd.read_csv('D:/333.csv', sep=",", header=None, encoding='utf-8')
# print(df)