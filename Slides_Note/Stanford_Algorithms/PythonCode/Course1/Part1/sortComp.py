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
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    mid = arrayLen // 2
    left = array[:mid]
    right = array[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)

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

print('Origin: {},\nSorted: {}'.format(originArray, sortedArray1))
print('Merge Sort takes {} sec'.format(end1-start1))
print('Selection Sort takes {} sec'.format(end2-start2))
print('Bubble Sort takes {} sec'.format(end3-start3))