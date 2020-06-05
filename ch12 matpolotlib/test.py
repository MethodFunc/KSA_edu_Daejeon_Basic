import numpy as np
import csv

class Prac_Files:
    def __init__(self):
        self.f = open('doctor_2019.csv', 'r', encoding='utf-8')

    def header(self, f):
        lines = csv.reader(self.f)
        header = next(lines)
        data_set = np.array([header])
        data_set = np.delete(data_set, 1)
        return data_set

    def location_sum(self, f, location):
        data_set = [0, 0, 0, 0]
        lines = csv.reader(self.f)

        for line in lines:
            if line[0] == location:
                for i in range(len(data_set)):
                    data_set[i] += int(line[i + 2])
        return data_set

    def close(self):
        self.f.close()


f = Prac_Files();
data = np.empty((0, 5))
data = np.append(data, f.header(f))
location = ['서울', '부산', '대구', '인천', '대전', '광주', '울산']
for i in range(len(location)):
    f = Prac_Files();
    data = np.append(data, location[i])
    data = np.append(data, f.location_sum(f, location[i]))
data = data.reshape(8, 5).tolist()

for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j], end=' ')
    print()

f.close()