# -*- coding: utf-8 -*-
"""
(original code running in Python2)
https://gist.github.com/aymanfarhat/6098683
@author: HYJ
"""


import random

# From txt to graph
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
    
    for k, l in g.items():
        g[k] = [edge[0] if x == edge[1] else x for x in g[k]]
    
    # Remove all edges of v1 to itself(loops)
    g[edge[0]] = [x for x in g[edge[0]] if x != edge[0]]
    
# Gets a random edge available in the current graph
def get_random_edge():
    v1 = list(g.keys()) [random.randint(0,len(g)-1)]
    v2 = g[v1] [random.randint(0,len(g[v1])-1)]
    return (v1,v2)

minlist = []

for i in range(0,100): # python3
    g = load_graph()

    # Keep contracting the graph until we have 2 vertices
    while(len(g) > 2):
        contract_edge(get_random_edge())
    
    minlist.append(len(g[list(g.keys())[0]]))

print(min(minlist))