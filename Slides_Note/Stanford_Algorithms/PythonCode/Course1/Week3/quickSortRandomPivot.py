# -*- coding: utf-8 -*-
"""
@author: HYJ
存在bug，还未全部修改
"""
import random
import math

## In-place Quick Sort with Randomization
def myRandomInt(lo, hi):
    return lo + math.floor(random.random()*(hi-lo))

def partitionRandom(array):
    arrayLen = len(array)
    randomPivot = myRandomInt(0, arrayLen)
    array[randomPivot], array[0] = array[0], array[randomPivot]
    pivotIndex = 0
    storeIndex = 0
    pivot = array[:pivotIndex+1]
    for i in range(storeIndex+1, arrayLen):
        if array[i] < array[pivotIndex]:
            storeIndex += 1
            array[i], array[storeIndex] = array[storeIndex], array[i]
    array[storeIndex], array[pivotIndex] = array[pivotIndex], array[storeIndex]
    lo = array[:storeIndex]
    hi = array[storeIndex+1:]
    return lo, hi, pivot

def quickSortRandom(array):
    sortedArray = []
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    if arrayLen == 2:
        if array[1] < array[0]:
            array[0], array[1] = array[1], array[0]
        return array
    lo, hi, pivot = partitionRandom(array)
    lo = quickSortRandom(lo)
    hi = quickSortRandom(hi)
    sortedArray = lo
    sortedArray.extend(pivot)
    sortedArray.extend(hi)
    return sortedArray

originArray = eval(input('input an array: '))

sortedArray = quickSortRandom(originArray)

print('Sorted array is {}'.format(sortedArray))