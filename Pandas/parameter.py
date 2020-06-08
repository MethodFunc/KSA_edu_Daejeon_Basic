import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random as rd
# 화면에 그래프 그리기
# %matplotlib inline
# Korean Setting , Minus 표시
mpl.rcParams['axes.unicode_minus'] = False
# family = 폰트 이름 size = 사이즈 크기
mpl.rc('font', family='D2Coding', size=25)
# Graph 크기 변경
plt.rcParams["figure.figsize"]= (15,9)


hightschool = pd.read_csv('high_school_2019.csv')

df = hightschool.iloc[:, 2:]
print(df)

df = pd.read_csv('population_age_2020.csv', thousands=',')