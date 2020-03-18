# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:06:16 2020

@author: HYJ
"""

## In-place Quick Sort
# 就是相当于一直翻转，最后一个即为当前的最大值
def partition(array):
    arrayLen = len(array)
    storeIndex = 0
    for i in range(1, arrayLen):
        if array[i] < array[storeIndex]:
            if i > storeIndex+1:
                array[i], array[storeIndex+1] = array[storeIndex+1], array[i]
            storeIndex += 1
    array[0], array[storeIndex] = array[storeIndex], array[0]
    lo = array[:storeIndex]
    hi = array[storeIndex+1:]
    return lo, hi, array[:1]

def quickSort(array):
    sortedArray = []
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    if arrayLen == 2:
        if array[1] < array[0]:
            array[0], array[1] = array[1], array[0]
        return array
    pivot = array[0]
    lo, hi, _ = partition(array)
    lo = quickSort(lo)
    hi = quickSort(hi)
    sortedArray = lo
    sortedArray.append(pivot)
    sortedArray.extend(hi)
    return sortedArray

originArray = eval(input('input an array: '))

sortedArray = quickSort(originArray)

print('Sorted array is {}'.format(sortedArray))