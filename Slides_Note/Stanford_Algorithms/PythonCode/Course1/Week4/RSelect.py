# -*- coding: utf-8 -*-
"""
@author: HYJ
"""

import math

## Randomnized Selection
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

def RSelect(array, length, order):
    if length == 1:
        return array[0]
    array = choosePivot(array, length, 3)
    #print(array)
    array, storeIndex = partition(array)
    if storeIndex == order-1:
        return array[storeIndex]
    elif storeIndex > order-1:
        return RSelect(array[:storeIndex], storeIndex, order)
    elif storeIndex < order-1:
        return RSelect(array[storeIndex+1:], length-storeIndex-1, order-storeIndex-1)


#file_name = "QuickSort.txt"
#num = []
#file = open(file_name, mode='r')
#for line in file:
#    line = line.split()
#    num.append(eval(line[0])) # 每一行类似是 ['1.1']
#file.close()
#order = 10000

num = [3,6,5,4]
order = 4
#originArray = eval(input('Input array: '))


num = RSelect(num, len(num),order)
print('No.{} in the array is {}'.format(order, num))