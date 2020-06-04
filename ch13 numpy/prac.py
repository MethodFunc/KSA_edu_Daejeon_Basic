import numpy as np
import csv

f = open('high_school_2019.csv', 'r', encoding='utf-8')
list_data=[]
lines = csv.reader(f)
header = next(lines)

for line in lines:
    list_data.append(line[:])

size = len(list_data)
data = np.zeros((size, 3), dtype='int32')
print(data)