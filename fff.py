
import codecs
import numpy as np

filename1 = "D:/5555.txt"

sd = list()
with codecs.open(filename1, 'r', 'utf-8') as f:
    lines1 = f.readlines()

for line in lines1:
    sd.append(float(line.strip()))
print(np.mean(sd))
print(np.var(sd))
print(np.std(sd))