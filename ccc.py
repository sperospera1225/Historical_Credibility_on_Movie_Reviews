import codecs
import numpy as np

filename1 = "D:/movie_review/new_data_review/the_outlaws/baseline_old/1_10_tt.txt"

arr5 = list()
arr10 = list()
arr15 = list()
arr20 = list()
arr25 = list()
arr30 = list()
arr35 = list()
arr40 = list()
arr45 = list()
arr50 = list()
arr55 = list()
arr60 = list()
arr65 = list()
arr70 = list()
arr75 = list()
arr80 = list()
arr85 = list()
arr90 = list()
arr95 = list()
arr100 = list()

with codecs.open(filename1, 'r', 'utf-8') as f:
    lines1 = f.readlines()

for line in lines1:
    if float(line.strip()) <= 5:
        arr5.append(float(line.strip()))
    elif float(line.strip()) <= 10:
        arr10.append(float(line.strip()))
    elif float(line.strip()) <= 15:
        arr15.append(float(line.strip()))
    elif float(line.strip()) <= 20:
        arr20.append(float(line.strip()))
    elif float(line.strip()) <= 25:
        arr25.append(float(line.strip()))
    elif float(line.strip()) <= 30:
        arr30.append(float(line.strip()))
    elif float(line.strip()) <= 35:
        arr35.append(float(line.strip()))
    elif float(line.strip()) <= 40:
        arr40.append(float(line.strip()))
    elif float(line.strip()) <= 45:
        arr45.append(float(line.strip()))
    elif float(line.strip()) <= 50:
        arr50.append(float(line.strip()))
    elif float(line.strip()) <= 55:
        arr55.append(float(line.strip()))
    elif float(line.strip()) <= 60:
        arr60.append(float(line.strip()))
    elif float(line.strip()) <= 65:
        arr65.append(float(line.strip()))
    elif float(line.strip()) <= 70:
        arr70.append(float(line.strip()))
    elif float(line.strip()) <= 75:
        arr75.append(float(line.strip()))
    elif float(line.strip()) <= 80:
        arr80.append(float(line.strip()))
    elif float(line.strip()) <= 85:
        arr85.append(float(line.strip()))
    elif float(line.strip()) <= 90:
        arr90.append(float(line.strip()))
    elif float(line.strip()) <= 95:
        arr95.append(float(line.strip()))
    elif float(line.strip()) <= 100:
        arr100.append(float(line.strip()))

print(len(arr5))
print(len(arr10))
print(len(arr15))
print(len(arr20))
print(len(arr25))
print(len(arr30))
print(len(arr35))
print(len(arr40))
print(len(arr45))
print(len(arr50))
print(len(arr55))
print(len(arr60))
print(len(arr65))
print(len(arr70))
print(len(arr75))
print(len(arr80))
print(len(arr85))
print(len(arr90))
print(len(arr95))
print(len(arr100))
