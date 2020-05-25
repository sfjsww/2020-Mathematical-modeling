import numpy as  np
import pandas as pd


def distance(x1,x2,y1,y2):
    d = np.sqrt(np.square(x1-x2)+np.square(y1-y2))
    return d

class node:
    belong = 0
    long = 0
    Num = 0
    count = 0
    def __init__(self,belong,long,Num):
        self.belong = belong
        self.long = long
        self.Num = Num
        self.count += 1


Vdata = pd.read_csv('数据.csv')

waitTotraverse ={}   #未遍历过的点的集合
i = 14
while i<=181:
    waitTotraverse[i] = node(0,0,i)
    i+=1


Traversed = {}
i = 2               #已遍历过的点的集合
while i<=13:
    Traversed[i] = node(i,0,i)
    i+=1

todeal = {}
node1 = 0  # 已遍历的连接点
node2 = 0  # 未遍历的连接点
line = []
cost = []

def connect(Traversed,waitTotraverse,todeal):
    if waitTotraverse:
        print(waitTotraverse.keys())
        min_d = 25.001  # 初始化最小距离
        l = 0
        p = 0
        for e in waitTotraverse:
            for m in Traversed:
                if distance(Vdata['X坐标'][e], Vdata['X坐标'][m], Vdata['Y坐标'][e], Vdata['Y坐标'][m]) <= min_d:
                    min_d = distance(Vdata['X坐标'][e], Vdata['X坐标'][m], Vdata['Y坐标'][e], Vdata['Y坐标'][m])
                    l = e
                    p = m
        if p != 0:
            if Traversed[Traversed[p].belong].long + min_d <= 40 and min_d != 25.001:
                node1 = p
                node2 = l
                Traversed[Traversed[p].belong].long += min_d
                del waitTotraverse[l]
                Traversed[l] = node(Traversed[p].belong,0,l)
                line.append([node1,node2])
                cost.append(min_d)
                return connect(Traversed,waitTotraverse,todeal)
            else:
                if l != 0:
                    todeal[l] = node(0, 0, l)
                    del waitTotraverse[l]
                    return connect(Traversed, waitTotraverse, todeal)
                else:
                    print(1)
                    return todeal.keys() | waitTotraverse.keys()
        else:
            return todeal.keys() | waitTotraverse.keys()
    print('V-P最短总路程为：', sum(cost))
    print('V-P代价', cost)
    print('V-P连线', line)
    print(todeal.keys() | waitTotraverse.keys())
    return todeal.keys() | waitTotraverse.keys()

#def Prim(e,G):
#    U = set(G.keys())
#    V = set((e,))
#    min_tree = []
#    cost = []
#    count = 0
#    while U.difference(V):
#        min_value = float("inf")
#        node1 = None
#        node2 = None
#        for v in V:
#            for u in U.difference(V):
#                if u in G[v]:
#                    if G[v][u] < min_value:
#                        if sum(cost)+min_value <=40:
#                            min_value = G[v][u]
#                            node1 = v
#                            node2 = u
#                            count += 1
#                            print(count)
#                        else:
#                            return count
#        V.add(node2)
#        min_tree.append([node1, node2])
#        cost.append(min_value)
#    return count
#
#def dense(list):
#    if len(list) != 1:
#        dict = {}
#        for e in list:
#            dic = {}
#            h = list
#            for a in h:
#                d = {}
#                for i in h:
#                    if a != i:
#                        d[i] = distance(Vdata['X坐标'][i], Vdata['X坐标'][a], Vdata['Y坐标'][i], Vdata['Y坐标'][a])
#                dic[a] = d
#            dict[e] = Prim(e,dic)
#        p = max(dict, key=dict.get)
#    return p

def dense(list):
    if len(list) != 1:
        dict = {}
        tmp4 = {}
        averagemin = 0
        for n in list:
            tmp = []
            for m in list:
                if n != m:
                    tmp.append(distance(Vdata['X坐标'][n], Vdata['X坐标'][m], Vdata['Y坐标'][n], Vdata['Y坐标'][m]))
            tmp.sort()
            tmp4[n] = tmp
        for e in tmp4:
            tmp_min = 0
            count = 0
            for i in tmp4[e]:
                if tmp_min+i < 50:
                    tmp_min += i
                    count += 1
            if count == 0:
                dict[e] = 100
            else:
                dict[e] = tmp_min/count
        for a in dict:
            if dict[a]>=averagemin:
                p = a
                averagemin = dict[a]
    else:
        for e in list:
            p = e
    return p


#if __name__ == '__main__':
#    t = {19, 22, 23, 24, 29, 30, 164, 165, 36, 167, 48, 55, 67, 69, 77, 84, 89, 122}      #未遍历
#    tmp1 = {}
#    for e in t:
#        tmp1[e] = node(0,0,e)
#    tmp2 = {}
#    tmp2[137] = node(137,0,137)     #已遍历
#    tmp3 = {}      #待处理
#    list = connect(tmp2, tmp1,tmp3)
#    while list:
#        tmp1 = {}
#        tmp2 = {}
#        tmp3 = {}
#        for e in list:
#            tmp1[e] = node(0,0,e)
#        a = dense(list)
#        del tmp1[a]
#        tmp2[a] = node(a,0,a)
#        list = connect(tmp2,tmp1,tmp3)
#        print(a)
#        print(list)

if __name__ == '__main__':
    tmp1 = {}  # 未遍历
    tmp2 = {}  # 已遍历
    tmp3 = {}  # 待处理
    list = connect(Traversed, waitTotraverse, todeal)
    while list:
        tmp1 = {}
        tmp2 = {}
        tmp3 = {}
        for e in list:
            tmp1[e] = node(0, 0, e)
        a = dense(list)
        del tmp1[a]
        tmp2[a] = node(a, 0, a)
        list = connect(tmp2, tmp1, tmp3)
        print(a)
        print(list)

    #while list:
    #    del tmp1[dense(list)]
    #    tmp2[dense(list)] = node(dense(list),0,dense(list))
    #    Numlist.append(dense(list))
    #    list = connect(tmp2, tmp1)
    #    count += 1
    #    print(tmp1.keys())
    #print(count)

if __name__ == '__main__':
    tmp1 = waitTotraverse      #未遍历
    tmp2 = Traversed      #已遍历
    tmp3 = {}      #待处理
    i = 1
    while i<=2:
        a = dense(tmp1)
        del tmp1[a]
        tmp2[a] = node(a, 0, a)
        print(a)
        i+=1
    connect(tmp2, tmp1,tmp3)



#if __name__ == '__main__':
#    tmp1 = waitTotraverse
#    tmp2 = Traversed
#    tmp3 = {}
#    linedis = {}
#    connect(tmp2,tmp1,tmp3)
#    for e in tmp3.keys():
#        tmp = {}
#        for i in tmp2.keys():
#            d = distance(Vdata['X坐标'][e], Vdata['X坐标'][i], Vdata['Y坐标'][e], Vdata['Y坐标'][i])
#            tmp[i] = d
#        linedis[e] = tmp
#    for a in linedis:
#        b = sorted(linedis[a].items(), key=lambda x: x[1])
#        for c in b:
#            if tmp2[tmp2[c[0]].belong].long + linedis[a][c[0]] <= 40:
#
#                node1 = c[0]
#                node2 = a
#                tmp2[tmp2[c[0]].belong].long += linedis[a][c[0]]
#                del tmp3[a]
#                tmp2[a] = node(tmp2[c[0]].belong, 0, a)
#                line.append([node1, node2])
#                cost.append(linedis[a][c[0]])
#    while tmp3:
#        tmp1 = {}
#        tmp2 = {}
#        tmp4 = {}
#        for e in tmp3:
#            tmp1[e] = node(0,0,e)
#        a = dense(list)
#        del tmp1[a]
#        tmp2[a] = node(a,0,a)
#        tmp3 = connect(tmp2,tmp1,tmp4)
#        print(a)
#        print(list)