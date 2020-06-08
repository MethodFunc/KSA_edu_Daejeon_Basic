def get_list(list_data):
    import csv
    f = open('population_2020.csv', 'r', encoding='utf-8')
    lines = csv.reader(f)
    header = next(lines)

    list_temp = []

    for line in lines:
        list_temp.append(line[:])

    for i in range(len(line)):
        tmp = []
        for j in range(len(list_temp)):
            tmp.append(list_temp[j][i])
        list_data.append(tmp)

def get_area(data):
    tmp = []
    for x in data:
        arr = x.split()
        tmp.append(arr[0])
    return tmp

def del_comma(data, t):
    tmp = []
    for x in data:
        string = ''
        arr = x.split(',')
        for i in range(len(arr)):
            string += arr[i]

        if t == 'integer':
            tmp.append(int(string))
        else:
            tmp.append(float(string))
    return tmp

def get_dict(list_data, key, dic_data):
    area = get_area(list_data[0])
    dic_data.update({key[0]:area})
    for i in range(1, 7):
        if i == 3 or i == 6:
            data = del_comma(list_data[i], 'float')
        else:
            data = del_comma(list_data[i], 'integer')
        dic_data.update({key[i]:data})



