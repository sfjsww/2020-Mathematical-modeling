import numpy as  np
import pandas as pd
from thirdQuestion1 import distance

list = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 48, 52, 55, 56, 58, 61, 62, 63, 64, 67, 69, 71, 74, 75, 77, 79, 80, 81, 82, 83, 84, 89, 90, 93, 94, 95, 96, 99, 100, 101, 102, 103, 104, 105, 107, 109, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 129, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 142, 143, 144, 145, 149, 150, 151, 155, 156, 157, 162, 163, 164, 165, 167, 168, 176, 177, 178, 179, 180, 181]
Vdata = pd.read_csv('数据.csv')

def dense(list):
    tmp = 0
    for n in list:
        count = 0
        for m in list:
            if n != m:
                if distance(Vdata['X坐标'][n], Vdata['X坐标'][m], Vdata['Y坐标'][n], Vdata['Y坐标'][m])<=15:
                    count += 1
        if count > tmp:
            tmp = count
            p = n
    return p

print(dense(list))


