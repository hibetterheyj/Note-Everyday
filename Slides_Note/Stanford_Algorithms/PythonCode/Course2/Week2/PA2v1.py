# -*- coding: utf-8 -*-
"""
modified from https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
"""
# https://docs.python.org/zh-cn/3/library/heapq.html
import heapq

"""Load graph"""
testFile = "problem9.8test.txt"
challengeFile = "dijkstraData.txt"
def load_graph():
    return {int(line.rstrip().split()[0]): {int(pair.split(',')[0]):int(pair.split(',')[1]) for pair in line.rstrip().split()[1:]}
            for line in open(challengeFile)}


def calculate_distances(graph, starting_vertex):
    # 初始化所有值为无穷大，并且起始点自身为0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

#test
testGraph = load_graph()
#Answer, for vertices 1 through 8, in order: 0,1,2,3,4,4,3,2.
#print(calculate_distances(testGraph, 1))
#sDis = calculate_distances(testGraph, 1)
#print([value for key,value in sDis.items()])

#challenge
challengeGraph = load_graph()
sDis = calculate_distances(challengeGraph, 1)
targetV = [7,37,59,82,99,115,133,165,188,197]
result = []
for i in range(len(targetV)):
    result.append(sDis[targetV[i]])
#print(result)
strResult = [str(j) for j in result]
print(','.join(strResult))