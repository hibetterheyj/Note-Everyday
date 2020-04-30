# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:04:22 2020

@author: HYJ
"""

"""Load graph"""
testFile = "problem9.8test.txt"
challengeFile = "dijkstraData.txt"
# 第二种写法
f=open(challengeFile,'r')
data = f.readlines()
# int(line.rstrip().split()[0])取出每行第一个数
# a = data[50].rstrip().split()[1:] 之后的连接与键值对
# {int(pair.split(',')[0]):int(pair.split(',')[1]) for pair in a}
#    可以得到
#    {5: 22,
#     10: 5578,
#     26: 9329,
#     31: 3739,
#     67: 4225}
def load_graph():
    return {int(line.rstrip().split()[0]): {int(pair.split(',')[0]):int(pair.split(',')[1]) for pair in line.rstrip().split()[1:]}
            for line in open(testFile)}
a = load_graph()
print(a)
    
