# -*- coding: utf-8 -*-
"""
@author: HYJ
"""
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

# 可以将输入直接转列表
originArray = eval(input('input an array: '))

start1 = time.clock()
sortedArray1 = mergeSort(originArray)
end1 = time.clock()

start2 = time.clock()
sortedArray2 = selectionSort(originArray)
end2 = time.clock()

start3 = time.clock()
sortedArray3 = selectionSort(originArray)
end3 = time.clock()

start4 = time.clock()
sortedArray4 = quickSort(originArray)
end4 = time.clock()

print('Sorted array is {}'.format(sortedArray4))
print('Merge Sort takes {} sec'.format(end1-start1))
print('Selection Sort takes {} sec'.format(end2-start2))
print('Bubble Sort takes {} sec'.format(end3-start3))
print('Quick Sort takes {} sec'.format(end3-start3))