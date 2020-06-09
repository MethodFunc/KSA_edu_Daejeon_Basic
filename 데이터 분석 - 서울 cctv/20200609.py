import pandas as pd
import numpy as np
import random as rd
import matplotlib as mpl
import matplotlib.pyplot as plt
# 화면에 그래프 그리기
# %matplotlib inline
# Korean Setting , Minus 표시
mpl.rcParams['axes.unicode_minus'] = False
# family = 폰트 이름 size = 사이즈 크기
mpl.rc('font', family='D2Coding', size=25)
# Graph 크기 변경
plt.rcParams["figure.figsize"]= (15,9)

pop = pd.read_csv('서울시 인구현황.txt', skiprows=[0] ,sep="\t", thousands=',', usecols=1)

pop = pd.read_excel('서울시 자치구 년도별 CCTV 설치 현황.xlsx')
pop.replace