import codecs
import numpy as np

filename1 = "D:/movie_review/new_data_review/confidential assignment/baseline_old/ut_0_10_sympathy_3.txt"

arr10 = list()
arr20 = list()
arr30 = list()
arr40 = list()
arr50 = list()
arr60 = list()
arr70 = list()
arr80 = list()
arr90 = list()
arr100 = list()

with codecs.open(filename1, 'r', 'utf-8') as f:
    lines1 = f.readlines()

for line in lines1:
    if float(line.strip()) <= 10:
        arr10.append(float(line.strip()))
    elif float(line.strip()) <= 20:
        arr20.append(float(line.strip()))
    elif float(line.strip()) <= 30:
        arr30.append(float(line.strip()))
    elif float(line.strip()) <= 40:
        arr40.append(float(line.strip()))
    elif float(line.strip()) <= 50:
        arr50.append(float(line.strip()))
    elif float(line.strip()) <= 60:
        arr60.append(float(line.strip()))
    elif float(line.strip()) <= 70:
        arr70.append(float(line.strip()))
    elif float(line.strip()) <= 80:
        arr80.append(float(line.strip()))
    elif float(line.strip()) <= 90:
        arr90.append(float(line.strip()))
    elif float(line.strip()) <= 100:
        arr100.append(float(line.strip()))

print(len(arr10))
print(len(arr20))
print(len(arr30))
print(len(arr40))
print(len(arr50))
print(len(arr60))
print(len(arr70))
print(len(arr80))
print(len(arr90))
print(len(arr100))
