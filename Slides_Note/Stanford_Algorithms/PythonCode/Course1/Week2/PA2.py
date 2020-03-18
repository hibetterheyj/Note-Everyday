# -*- coding: utf-8 -*-
"""
Solution for PA#2

# reference
1. 用python从txt文件中读入数据
https://blog.csdn.net/LCCFlccf/article/details/82683725
"""
import time

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

file_name = "IntegerArray.txt"
num = []
file = open(file_name, mode='r')
for line in file:
    line = line.split()
    num.append(eval(line[0])) # 每一行类似是 ['1.1']
file.close()
txtnum = len(num)

originArray = num
start = time.clock()
_, Inversions = sortCount(originArray)
end = time.clock()

print('Origin array with {} numbers has {} inversions.'.format(txtnum, Inversions))
print('It takes {} sec to count'.format(end-start))
