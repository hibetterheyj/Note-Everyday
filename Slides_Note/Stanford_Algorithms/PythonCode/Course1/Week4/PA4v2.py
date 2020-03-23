# -*- coding: utf-8 -*-
"""
(original code running in Python2)
https://gist.github.com/aymanfarhat/6098683
@author: HYJ
"""


import random

# 生成包含list的dict
# From txt to graph
def load_graph():
    return {int(line.rstrip().split()[0]): [int(i) for i in line.rstrip().split()[1:]] for line in
       open("./kargerMinCut.txt")}
"""
## 字典 dict
# 取单一个值：
两种方式访问 dict.get(index) 或者 dict[key]
# 遍历：
获取所有 dict.items()
循环遍历
for key, value in dict.items():
    print(key, value)
# 访问键/值
list(dict.keys()) # 访问所有的值并且转化为list
list(dict.values()) # 访问所有的值并且转化为list
# 删除
del dict[key]
"""

# Contract an edge between 2 vertices
def contract_edge(edge): # edge = (v1,v2)
    global g
    
    # merge v2 into v1 and remove v2 from graph
    v1l = g[edge[0]]
    # 合并就是把另外一点的 adjacent list 合并过来
    v1l.extend(g[edge[1]])
    # 删掉原字典
    del g[edge[1]]
    
    # 更新 graph
    for k, l in g.items():
        g[k] = [edge[0] if x == edge[1] else x for x in g[k]] # for循环生成列表
    
    # 删除 self-loops
    # Remove all edges of v1 to itself(loops)
    g[edge[0]] = [x for x in g[edge[0]] if x != edge[0]] # for循环生成列表
    
# Gets a random edge available in the current graph
def get_random_edge():
#    v1 = list(g.keys()) [random.randint(0,len(g)-1)] # 随意选取当前的一个点
#    v2 = g[v1] [random.randint(0,len(g[v1])-1)] # 随意选取当前的一个点
    # 可以进一步优化，直接利用random.choice函数
    v1 = random.choice(list(g.keys()))
    v2 = random.choice(g[v1])
    return (v1,v2)

minlist = []
iters = 40

for i in range(0,iters): # python3
    g = load_graph()

    # Keep contracting the graph until we have 2 vertices
    # 结束条件就是还有两条边
    while(len(g) > 2):
        contract_edge(get_random_edge())
    
    minlist.append(len(g[list(g.keys())[0]]))
    if i%5==0:
        print('After {} iterations, current min is {}'.format(i+1, min(minlist)))

print('Final result of the min cut problem: {}'.format(min(minlist)))