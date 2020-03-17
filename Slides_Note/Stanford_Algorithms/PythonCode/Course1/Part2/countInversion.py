# -*- coding: utf-8 -*-
"""
@author: HYJ

modified from Merge Sort
"""

## Merge Sort adding Count
def merge(left, right):
    result = []
    countInv = 0
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            countInv += len(left) # 相当于加上 left 剩下的个数
            result.append(right.pop(0))
    # 只要 left 或者 right 非空
    if left:
        result += left
    if right:
        result += right
    return result, countInv

def sortCount(array):
    count = 0
    arrayLen = len(array)
    if arrayLen <= 1:
        return array, count
    elif arrayLen == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
            count += 1
            return array, count
        else:
            return array, count
    mid = arrayLen // 2
    left = array[:mid]
    right = array[mid:]
    
    left, leftInv = sortCount(left)
    right, rightInv = sortCount(right)
    
    array, mergeInv = merge(left, right)
    count = leftInv+rightInv+mergeInv
    return array, count
    
originArray = eval(input('input an array: '))
_, Inversions = sortCount(originArray)

print('Array {} has {} Inversions.'.format(originArray, Inversions))
    