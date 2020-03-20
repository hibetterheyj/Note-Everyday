# -*- coding: utf-8 -*-
"""
@author: HYJ

1. Python3 求最大/小值及索引值 Numpy
https://blog.csdn.net/weixin_39223665/article/details/79675927
输入6，4会报错！
"""

import math

## In-place Quick Sort
# 就是相当于一直翻转，最后一个即为当前的最大值
def partition(array):
    pivotIndex = 0
    storeIndex = 0
    compTimes = 0
    pivot = array[pivotIndex:pivotIndex+1]
    for i in range(storeIndex+1, len(array)):
        if array[i] < array[pivotIndex]:
            storeIndex += 1
            array[i], array[storeIndex] = array[storeIndex], array[i]
        compTimes += 1
    array[storeIndex], array[pivotIndex] = array[pivotIndex], array[storeIndex]
    lo = array[:storeIndex]
    hi = array[storeIndex+1:]
    return lo, hi, pivot, compTimes

def choosePivot(array, length, method):
    # return pivot, index
    # case 1: first element
    # case 2: final element
    # case 3: median-of-three
    if method == 1:
        return array
    elif method == 2:
        array[length-1], array[0] = array[0], array[length-1]
        return array
    elif method == 3:
        if length == 1 or length == 2:
            return array
        else: 
            middle = math.ceil(length/2)-1
            storeThree = [array[0], array[middle], array[length-1]]
            sortThree = [array[0], array[middle], array[length-1]]
            sortThree.sort()
            idx = storeThree.index(sortThree[1])
            if idx == 1:
                array[middle], array[0] = array[0], array[middle]
            elif idx == 2:
                array[length-1], array[0] = array[0], array[length-1]
            return array

def quickSort(array, length):
    sortedArray = []
    if length <= 1:
        return array, 0
    #if arrayLen == 2:
    #    if array[1] < array[0]:
    #        array[0], array[1] = array[1], array[0]
    #    return array
    array = choosePivot(array, length, 3)
    lo, hi, pivot, compTimes = partition(array)
    #print(lo)
    #print(hi)
    lo, loCompTimes = quickSort(lo, len(lo))
    hi, hiCompTimes = quickSort(hi, len(hi))
    sortedArray = lo
    sortedArray.extend(pivot)
    sortedArray.extend(hi)
    return sortedArray, compTimes + loCompTimes + hiCompTimes

#originArray = eval(input('Input array: '))
file_name = "QuickSort.txt"
num = []
file = open(file_name, mode='r')
for line in file:
    line = line.split()
    num.append(eval(line[0])) # 每一行类似是 ['1.1']
file.close()

sortedArray, compSum = quickSort(num, len(num))

# 1: 162085
# 2: 164123
# 3: 138382

#print('Sorted array: {}'.format(sortedArray))
print('It needs {} time(s) to compare!'.format(compSum))