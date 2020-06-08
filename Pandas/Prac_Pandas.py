import pandas as pd
import Prac_modules as md

list_data =[]

md.get_list(list_data)
print(list_data)

dict_data = {}

keys = ['지역','총인구수','세대수', '세대당_인구', '남자_인구수', '여자_인구수','남여_비율']

md.get_dict(list_data, keys, dict_data)

frame = pd.DataFrame(dict_data)
print(frame)