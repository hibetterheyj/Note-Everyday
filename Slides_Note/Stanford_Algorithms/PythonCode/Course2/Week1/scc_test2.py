# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:47:40 2020

@author: HYJ
1. 《python算法教程》Day7 - 获取有向图的所有强连通分量
https://www.jianshu.com/p/192ae0425917
2. python：如何将txt文件中的数值数据读入到list中
https://blog.csdn.net/littlle_yan/article/details/79302315
"""

from collections import defaultdict

def readGraph2Dict(reverse=False):
    graphDist = defaultdict(list)
    for line in open("./problem8.10test3.txt"):
#    for line in open("./SCC.txt"):
        lineSep = line.rstrip().split()
        edge = [int(lineSep[0]), int(lineSep[1])]
        if reverse:
            graphDist[edge[1]].append(edge[0])
        else:
            graphDist[edge[0]].append(edge[1])
    return graphDist



G = readGraph2Dict()
GT = readGraph2Dict(reverse=True)

#SCC.txt长度下
print(len(G))  # 739454
print(len(GT)) # 714547