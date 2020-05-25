import numpy as  np
import pandas as pd

c = pd.read_csv('数据A-V.csv')  # 读取训练数据
def distance(x1,x2,y1,y2):
    d = np.sqrt(np.square(x1-x2)+np.square(y1-y2))
    return d

i = 1
dict = {}
while i <= 13:
    d = {}
    a = 1
    while a<=13:
        if a == i:
            a = a + 1
        else:
            d[a] = distance(c['X坐标'][i],c['X坐标'][a],c['Y坐标'][i],c['Y坐标'][a])
            a = a + 1
    dict[i] = d
    i = i + 1
print(dict)

# python3改变了dict.keys,返回的是dict_keys对象,支持iterable 但不支持indexable，我们可以将其明确的转化成list：
# V = set(G.keys())[0]
# difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
"""
语法：set.difference(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 

print(z)  # {'cherry', 'banana'}返回一个集合，元素包含在集合 x ，但不在集合 y ：
"""


# python3改变了dict.keys,返回的是dict_keys对象,支持iterable 但不支持indexable，我们可以将其明确的转化成list：
# V = set(G.keys())[0]
# difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
def Prim(G):
    U = set(G.keys())  # 图G的顶点集合U，它包含了该图的所有顶点, 创建一个空集合必须用 set() 而不是 { }，
    # 因为 { } 是用来创建一个空字典。
    # V = set(list(U)[0])                      # 将起始顶点加入集合V,  集合对 list 和 tuple 具有排序(升序)
    V = set((1,))
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



if __name__ == '__main__':
    Prim(dict)