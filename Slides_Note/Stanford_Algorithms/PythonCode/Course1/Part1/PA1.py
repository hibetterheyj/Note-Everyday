# -*- coding: utf-8 -*-
"""
Solution for PA#1
"""

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

# For Coursera
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
# For General Purpose
# x = int(input('num1: '))
# y = int(input('num2: '))

xy1 = karatsubaMulti(x, y)

print('The result of {} times {} is {}'.format(x, y, xy1))