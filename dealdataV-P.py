import numpy as  np
import pandas as pd

c = pd.read_csv('数据.csv')  # 读取训练数据
def distance(x1,x2,y1,y2):
    d = np.sqrt(np.square(x1-x2)+np.square(y1-y2))
    return d


i = 1
dict = {}
while i <= 180:
    d = {}
    a = 1
    while a<=180:
        if a == i:
            a = a + 1
        else:
            d[a] = distance(c['X坐标'][i],c['X坐标'][a],c['Y坐标'][i],c['Y坐标'][a])
            a = a + 1
    dict[i] = d
    i = i + 1
print(dict)