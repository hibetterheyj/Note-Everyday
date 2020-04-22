# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:19:05 2020

@author: HYJ
1. 《python算法教程》Day7 - 获取有向图的所有强连通分量
https://www.jianshu.com/p/192ae0425917
2. python：如何将txt文件中的数值数据读入到list中
https://blog.csdn.net/littlle_yan/article/details/79302315

对于主文件和test4会报错！
"""

from collections import defaultdict

#获取翻转所有边的图
def tr(G):
    #初始化翻转边的图GT
    GT=dict()
    for u in G.keys():
        GT[u]=GT.get(u,set())
    #翻转边
    for u in G.keys():
        for v in G[u]:
            GT[v].add(u)
    return GT

#获取按节点遍历完成时间递减排序的顺序
def topoSort(G):
    res=[]
    S=set()
    #dfs遍历图
    def dfs(G,u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            if v in S:
                continue
            dfs(G,v)
        res.append(u)
    #检查是否有遗漏的节点
    for u in G.keys():
        dfs(G,u)
    #返回拓扑排序后的节点列表
    res.reverse()
    return res

#通过给定的起始节点，获取单个连通量
def walk(G,s,S=None):
    if S is None:
        s=set()
    Q=[]
    P=dict()
    Q.append(s)
    P[s]=None
    while Q:
        u=Q.pop()
        for v in G[u]:
            if v in P.keys() or v in S:
                continue
            Q.append(v)
            P[v]=P.get(v,u)
    #返回强连通图
    return P
    
#G={
#    'a':{'b','c'},
#    'b':{'d','e','i'},
#    'c':{'d'},
#    'd':{'a','h'},
#    'e':{'f'},
#    'f':{'g'},
#    'g':{'e','h'},
#    'h':{'i'},
#    'i':{'h'}
#}
# 这个版本仅对个位数有效！
def readGraph2Dict():
    graphDist = defaultdict(list)
    for line in open("./problem8.10test5.txt"):
        #print(line) # 样式 '9 3\n'
        edge = [int(line[0]), int(line[2])]
        graphDist[edge[0]].append(edge[1])
    return graphDist
# 参考进行优化！
#https://blog.csdn.net/littlle_yan/article/details/79302315
def readGraph2Dictv2(reverse=False):
    graphDist = defaultdict(list)
    for line in open("./problem8.10test4.txt"):
#    for line in open("./SCC.txt"):
        lineSep = line.rstrip().split()
        edge = [int(lineSep[0]), int(lineSep[1])]
        if reverse:
            graphDist[edge[1]].append(edge[0])
        else:
            graphDist[edge[0]].append(edge[1])
    return graphDist

G = readGraph2Dictv2()
GT = readGraph2Dictv2(reverse=True)
#print(G)

#记录强连通分量的节点
seen=set()
#储存强强连通分量
scc=[]
#GT=tr(G)
for u in topoSort(G):
    if u in seen :
        continue
    C=walk(GT,u,seen)
    seen.update(C)
    scc.append(sorted(list(C.keys())))

#print(scc)

def top5SCC(scc):
    lenList = []
    sccLen = len(scc)
    for i in range(sccLen):
        lenList.append(len(scc[i]))
    sortLen = sorted(lenList,reverse=True)
    if sccLen >= 5:
        return sortLen[:5]
    else:
        for i in range(5-sccLen):
            sortLen.append(0)
        return sortLen
        
    
print('Top 5 SCC sizes:',top5SCC(scc))
