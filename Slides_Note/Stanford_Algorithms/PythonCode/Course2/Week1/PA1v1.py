# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:23:49 2020

https://github.com/jelenalor/kosaraju_algorithm/blob/7803348c1e3f91560025794fe4488dda8cbc3581/kosaraju.py
"""

""" Python 3.7
Author - Jelena Lor 
Kosaraju's algorithm for finding strongly connected components SCC"""

import numpy as np


"""Load graph"""
with open(r"SCC.txt", "r") as f:
    data = f.readlines()

num_of_nodes = 875715
G = [set([]) for i in range(num_of_nodes)]
G_reverse = [set([]) for i in range(num_of_nodes)]

for line in data:
    item = line.split()
    G[int(item[0])].add(int(item[1]))
    G_reverse[int(item[1])].add(int(item[0]))

# ORDERING ALGORITHM
def dfs_iter(graph, s):
    global colors
    global ordering
    global t
    stack = [s]
    while stack:
        vertex = stack.pop()
        if colors[vertex] != "F":
            stack.append(vertex)
            if colors[vertex] == "U":
                colors[vertex] = "D"

            all_adj_discover = True
            for w in list(graph[vertex]):
                if colors[w] == "U":
                    stack.append(w)
                    all_adj_discover = False
            if all_adj_discover:
                colors[vertex] = "F"
                t = t + 1
                ordering[t] = vertex


def dfs(graph, num_of_nodes):
    global colors
    global ordering
    global t
    # U - undiscovered, D - discovered, F - finished
    colors = ["U"] * num_of_nodes
    ordering = [0] * num_of_nodes
    t = 0
    for u in range(1, num_of_nodes)[::-1]:
        if colors[u] == "U":
            dfs_iter(graph, u)
    return ordering


def dfs_scc(graph, num_of_nodes, magical_ordering):
    global colors
    global lead_scc
    global t
    # U - undiscovered, D - discovered, F - finished
    colors = ["U"] * num_of_nodes
    lead_scc = [0] * num_of_nodes
    for u in magical_ordering:
        #         print("u %s" %u)
        if colors[u] == "U":
            lead_scc[u] = u
            dfs_iter_scc(graph, u)

    return lead_scc


def dfs_iter_scc(graph, s):
    global colors
    global lead_scc
    global t
    stack = [s]
    while stack:
        vertex = stack.pop()
        if colors[vertex] != "D":
            stack.append(vertex)
            if colors[vertex] == "U":
                colors[vertex] = "D"
                lead_scc[vertex] = s
            for w in list(graph[vertex]):
                if colors[w] == "U":
                    stack.append(w)


# ALGORITHM
# Find ordering of nodes by its finishing times
ordering = dfs(G_reverse, 875715)
# Reverse the order of the finishing nodes
ordering.reverse()
# Find the leading node for each of the strongly connected component
lead_scc = dfs_scc(G, 875715, ordering)
# Find the size of the top 5 largest strongly connected components
value, counts = np.unique(lead_scc, return_counts=True)
counts.sort()
print(counts[-5:])