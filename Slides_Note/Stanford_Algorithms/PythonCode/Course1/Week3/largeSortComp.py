# -*- coding: utf-8 -*-
"""
@author: HYJ
"""

import random
import math
import time

## MergeSort
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只要 left 或者 right 非空
    if left:
        result += left
    if right:
        result += right
    return result

def mergeSort(array):
    sortedArray = []
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    mid = arrayLen // 2
    left = array[:mid]
    right = array[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    sortedArray = merge(left, right)
    return sortedArray

## Selection Sort
# 就是每次找到最小的，然后一直和开头进行交换
def selectionSort(array):
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    for i in range(arrayLen-1):
        minIndex = i # <= i的数值是已经排序的
        for j in range(i+1,arrayLen):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array

## Bubble Sort
# 就是相当于一直翻转，最后一个即为当前的最大值
def bubbleSort(array):
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    for i in range(arrayLen-1):
        for j in range(arrayLen-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array

## In-place Quick Sort
def partition(array):
    arrayLen = len(array)
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

def quickSort(array):
    sortedArray = []
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    if arrayLen == 2:
        if array[1] < array[0]:
            array[0], array[1] = array[1], array[0]
        return array
    lo, hi, pivot = partition(array)
    lo = quickSort(lo)
    hi = quickSort(hi)
    sortedArray = lo
    sortedArray.extend(pivot)
    sortedArray.extend(hi)
    return sortedArray

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

file_name = "IntegerArray.txt"
num = []
file = open(file_name, mode='r')
for line in file:
    line = line.split()
    num.append(eval(line[0])) # 每一行类似是 ['1.1']
file.close()

start1 = time.clock()
sortedArray1 = quickSort(num)
end1 = time.clock()

start2 = time.clock()
sortedArray2 = mergeSort(num)
end2 = time.clock()

print('Result equals or not? {}'.format(sortedArray1 == sortedArray2))
print('In-place Quick Sort takes {} sec'.format(end1-start1))
print('Merge Sort takes {} sec'.format(end2-start2))
#print('Selection Sort takes {} sec'.format(end1-start1))
#print('Bubble Sort takes {} sec'.format(end3-start3))
#print('Quick Sort takes {} sec'.format(end3-start3))

