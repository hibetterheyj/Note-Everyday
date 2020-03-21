# -*- coding: utf-8 -*-
"""
Deterministic Selection
@author: HYJ
"""
import math
def middle(length):
    return math.ceil(length/2)

# 其实这一步可以直接sort
def QSort(array):
    if not array: # 如果是空集，则返回
        return array
    return (QSort([x for x in array[1:] if x<array[0]]) 
            + [array[0]] 
            + QSort([x for x in array[1:] if x>=array[0]]))

## Deterministic Selection
def partition(array):
    pivotIndex = 0
    storeIndex = 0
    #pivot = array[pivotIndex:pivotIndex+1]
    for i in range(storeIndex+1, len(array)):
        if array[i] < array[pivotIndex]:
            storeIndex += 1
            array[i], array[storeIndex] = array[storeIndex], array[i]
    array[storeIndex], array[pivotIndex] = array[pivotIndex], array[storeIndex]
    return array, storeIndex

def choosePivot(array, length, method):
    return 1

def DSelect(array, length, order):
    if length == 1:
        return array[0]
    groupNum = math.ceil(length/5) # 不应该是原有的length//5+1，而应该是向上取整
    subGroup = []
    for i in range(groupNum-1):
        subGroup.append(array[5*i: 5*i+5])
    subGroup.append(array[5*groupNum-5:])
    centerSet = []
    for sub in subGroup:
        sub.sort()
        centerSet.append(sub[middle(len(sub))-1])
    pivot = DSelect(centerSet, groupNum, middle(groupNum))
    idx = array.index(pivot)
    #print(arrayp[idx])
    array[0], array[idx] = array[idx], array[0]
    array, storeIndex = partition(array)
    if storeIndex == order-1:
        return array[storeIndex]
    elif storeIndex > order-1:
        return DSelect(array[:storeIndex], storeIndex, order)
    elif storeIndex < order-1:
        return DSelect(array[storeIndex+1:], length-storeIndex-1, order-storeIndex-1)

file_name = "QuickSort.txt"
array = []
file = open(file_name, mode='r')
for line in file:
    line = line.split()
    array.append(eval(line[0])) # 每一行类似是 ['1.1']
file.close()
order = 1000

#array = eval(input('Input array: '))
#array = [3,6,5,100,20,14,26,15,12,11,7,29,77,89,64,101,13,21]
#order =  # 超过9就报错！

result = DSelect(array, len(array), order)
print('No.{} in the array is {}'.format(order, result))