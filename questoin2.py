import numpy as  np
import pandas as pd
c=np.loadtxt('ZXY.txt',dtype = int)  # 读取训练数据
def distance(x1,x2,y1,y2):
    d = np.sqrt(np.square(x1-x2)+np.square(y1-y2))
    return d
i = 0
dict = {}

#graph
while i < 180:
    d = {}
    a = 0
    while a < 180:
        if a == i:
            a = a + 1
        else:
            d[a] = distance(c[i][0], c[a][0], c[i][1], c[a][1])
            a = a + 1
    dict[i] = d
    i = i + 1



def Prim(G,num1,num2):
    U = set(G.keys())
    V=set((0,1,2,3,4,5,6,7,8,9,10,11,num1,num2))
    min_tree = []  # 存储要返回的最小生成树的所有的边
    cost = []  # 记录最小生成树各边的权重的值

    while U.difference(V):  # 当集合U和V不想等时，进入循环while U != V
        min_value = float("inf")  # 初始化一个最小值
        node1 = None  # 用于记录加入边的第一个节点
        node2 = None  # 用于记录加入边的第二个节点
        for v in V:  # 遍历访问过的节点
            for u in U.difference(V):  # 遍历未访问过的节点
                if u in G[v]:  # 如果两个节点之间存在相连的边
                    if G[v][u] < min_value:  # 判断该值是否是所有访问过节点存在的相邻边中的最小值
                        min_value = G[v][u]  # 更新边权重的最小值
                        node1 = v  # 记录边权重最小值的第一个节点
                        node2 = u  # 记录边权重最小值的第二个节点

        V.add(node2)  # 将第二个节点加入到访问过的节点集合V，因为第二个节点来自于未访问过的节点集合
        min_tree.append([node1, node2])  # 将包括两个节点的边加入到最小生成树边列表
        cost.append(min_value)  # 将边的权重加入到成本列表中

     print("普利姆Prim算法最小生成树：")
     print("各个边的权值: ", cost)
     print("最小生成树的成本: ", sum(cost))
     print("最小生成树的边: ", min_tree)
    return sum(cost)

if __name__ == '__main__':
    cost=[]
    train = 0  # 训练次数
    for num1 in range(12,180):
        for num2 in range(num1+1,180):
            train = train+1
            print("训练次数{}".format(train))
            print("升级的两个点为{} {}".format(num1,num2))

            loss = Prim(dict,num1,num2)
            print(loss)
            cost.append(loss)
    print("*******************")
    print(cost)
    print(min(cost))
    print(cost.index(min(cost)))



