# -*- coding: utf-8 -*-
"""
(original code running in Python2)
https://gist.github.com/aymanfarhat/6098683
@author: HYJ
"""


import random

# Load the file into a graph represented by a dict of lists
#import re # 正则化
#def load_graph():
#    g = {}
#
#    f = open('kargerMinCut.txt')
#    lines = f.readlines()
#    f.close()
#
#    lines = map(lambda s: re.sub('\s+',' ',str(s.strip('\r\n'))).strip(),lines)
#    lines = map(lambda s: s.split(' '),lines)
#
#    for line in lines:
#        g[int(line[0])] = map(lambda s: int(s),line[1:])
#    
#    return g
# comment
def load_graph():
    return {int(line.rstrip().split()[0]): [int(i) for i in line.rstrip().split()[1:]] for line in
       open("./kargerMinCut.txt")}

# Contract an edge between 2 vertices
def contract_edge(edge):
    global g 
    
    # merge v2 into v1 and remove v2 from graph
    v1l = g[edge[0]]
    v1l.extend(g[edge[1]])
    del g[edge[1]]
    
    #replace all occurnces of v2 value with v1
    # https://blog.csdn.net/shuiyixin/article/details/86741810
    # python3中已经没有 “iteritems” 这个属性了，现在属性是：“ items ” 。
    #for k, l in g.iteritems():
    for k, l in g.items():
        g[k] = [edge[0] if x == edge[1] else x for x in g[k]]
    
    # Remove all edges of v1 to itself(loops)
    g[edge[0]] = [x for x in g[edge[0]] if x != edge[0]]
    
# Gets a random edge available in the current graph
def get_random_edge():
# https://blog.csdn.net/weixin_42087090/article/details/81195470
#    v1 = g.keys() [random.randint(0,len(g)-1)]
    v1 = list(g.keys()) [random.randint(0,len(g)-1)]
    v2 = g[v1] [random.randint(0,len(g[v1])-1)]
    return (v1,v2)

minlist = []
# https://blog.csdn.net/weixin_44224529/article/details/89397855
# Repeat 10 times to get a minimum
#for i in xrange(0,20): # python2 
for i in range(0,100): # python3
    g = load_graph()

    # Keep contracting the graph until we have 2 vertices
    while(len(g) > 2):
        contract_edge(get_random_edge())
    
    minlist.append(len(g[list(g.keys())[0]]))

print(min(minlist))