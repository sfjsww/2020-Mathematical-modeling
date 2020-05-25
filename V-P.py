import numpy as  np
import pandas as pd

c = pd.read_csv('数据.csv')  # 读取训练数据
def distance(x1,x2,y1,y2):
    d = np.sqrt(np.square(x1-x2)+np.square(y1-y2))
    return d


i = 2
dict = {}
while i <= 181:
    d = {}
    a = 2
    while a<=181:
        if a == i:
            a = a + 1
        else:
            d[a] = distance(c['X坐标'][i],c['X坐标'][a],c['Y坐标'][i],c['Y坐标'][a])
            a = a + 1
    dict[i] = d
    i = i + 1



def Prim(G):
    U = set(G.keys())  # 图G的顶点集合U，它包含了该图的所有顶点, 创建一个空集合必须用 set() 而不是 { }，
    # 因为 { } 是用来创建一个空字典。
    # V = set(list(U)[0])                      # 将起始顶点加入集合V,  集合对 list 和 tuple 具有排序(升序)
    V = set((2,3,4,5,6,7,8,9,10,11,12,13))
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
    return cost, min_tree


def PrimSelf(G):
    U = set(G.keys())
    V = set(list(U)[0])
    tree = []
    cost = []

    while U != V:
        min_value = float("inf")
        node1, node2 = None, None
        for v in V:
            for u in U.difference(V):
                if u in G[v]:
                    if G[v][u] < min_value:
                        min_value = G[v][u]
                        node1 = v
                        node2 = u

        V.add(node2)
        tree.append([node1, node2])
        cost.append(min_value)


if __name__ == '__main__':
    Prim(dict)