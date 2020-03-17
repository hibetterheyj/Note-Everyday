# -*- coding: utf-8 -*-
"""
@author: HYJ

# reference
1. 几种Python执行时间的计算方法
https://blog.csdn.net/wangshuang1631/article/details/54286551
2. Karatsuba乘法算法二（python）
https://blog.csdn.net/weixin_42673883/article/details/81045387
"""
import time

def karatsubaMulti(num1, num2):
    len1 = len(str(num1))
    len2 = len(str(num2))
    #len1 = int(math.log10(x)) + 1
    #len1 = int(math.log10(x)) + 1
    if len1==1 or len2==1:
        return num1*num2
    maxLen = max(len1, len2)
    a = num1 // pow(10, maxLen//2)
    b = num1 %  pow(10, maxLen//2)
    c = num2 // pow(10, maxLen//2)
    d = num2 % pow(10, maxLen//2)
    z1 = karatsubaMulti(a, c)
    z2 = karatsubaMulti(b, d)
    z3 = karatsubaMulti(a+b, c+d)
    return z1 * pow(10, maxLen) + (z3-z1-z2) * pow(10, maxLen//2) + z2

def bruteForceMulti(num1, num2):
    len1 = len(str(num1))
    len2 = len(str(num2))
    #len1 = int(math.log10(x)) + 1
    #len1 = int(math.log10(x)) + 1
    if len1==1 or len2==1:
        return num1*num2
    maxLen = max(len1, len2)
    a = num1 // pow(10, maxLen//2)
    b = num1 %  pow(10, maxLen//2)
    c = num2 // pow(10, maxLen//2)
    d = num2 % pow(10, maxLen//2)
    z1 = bruteForceMulti(a, c)
    z2 = bruteForceMulti(b, d)
    z3 = bruteForceMulti(a, d) + bruteForceMulti(b, c)
    return z1 * pow(10, maxLen) + z3 * pow(10, maxLen//2) + z2

# For Coursera
# x = 3141592653589793238462643383279502884197169399375105820974944592
# y = 2718281828459045235360287471352662497757247093699959574966967627
# For General Purpose
x = int(input('num1: '))
y = int(input('num2: '))
## Karatsuba Multiplication
start1 = time.clock()
xy1 = karatsubaMulti(x, y)
end1 = time.clock()

## Brute Force Multiplication
start2 = time.clock()
xy2 = bruteForceMulti(x, y)
end2 = time.clock()

#print('The result of {} times {} is {}'.format(x, y, xy1))
print('Karatsuba Multiplication takes {} sec'.format(end1-start1))
print('Brute Force Multiplication takes {} sec'.format(end2-start2))

