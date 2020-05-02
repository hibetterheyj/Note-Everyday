# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:40:06 2020

@author: HYJ
"""

# https://blog.csdn.net/weixin_44026955/article/details/84921885
# 原方法无法计算出最小的那一对
def twoSum(array, tsum):
    hashMap = {}
    for i, num in enumerate(array):
        # 感觉得先构造map，词典 key 对应的 val 是他的索引
        hashMap[num] = i
    for i, num in enumerate(array):
        if tsum-num in hashMap:
            target = hashMap[tsum-num]
            return True, [array[i], array[target]]
    return False, []
# 只需构建一次，避免反复迭代！
def setHashMap(array):
    hashMap = {}
    for i, num in enumerate(array):
        # 感觉得先构造map，词典 key 对应的 val 是他的索引
        hashMap[num] = i
    return hashMap

def twoSumModified(array, tsum, hashMap):
    for i, num in enumerate(array):
        if tsum-num in hashMap:
            target = hashMap[tsum-num]
            return True, [array[i], array[target]]
    return False, []

testFile = "problem12.4test.txt"
challengeFile = "algo1-programming_prob-2sum.txt"
def loadArray(file):
    array = []
    for line in open(file):
        array.append(int(line.rstrip()))
    return array

if __name__ == '__main__':
#    nums = sorted(loadArray(testFile))
#    intervalMin = 3
#    intervalMax = 10
    # it tool almonst an hour to complete the search 
    nums = sorted(loadArray(challengeFile))
    intervalMin = -10000
    intervalMax = 10000
    hashMap = setHashMap(nums)
    success = 0
    for i in range(intervalMin, intervalMax+1):
        if i % 200 == 0:
            print('Current: {}, Percentage: {} %'.format(i,(i+10000)/200))
            print('Success:{}'.format(success))
        res, _ = twoSumModified(nums, i, hashMap)
        if res:
            success += 1
    print('Total:{}'.format(success))
#    Total:427