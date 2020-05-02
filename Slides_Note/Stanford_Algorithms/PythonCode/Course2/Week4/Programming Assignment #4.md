## Programming Assignment #4

1.Question 1

Download the following text file:

[algo1-programming_prob-2sum.txt](https://d3c33hcgiwev3.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_algo1-programming_prob-2sum.txt?Expires=1588550400&Signature=YBFWeGrAjYDZy8Trs4T17uHOVqRZs1OmBqhH0r2meN76pqt0DqZ9pHKM9MpYzXPXU9oZI9YOsTEbgY5Vvtuzr9P-gGewLRf7OboaqSscSZlumE7M2iPIYpoUS3cr8J5SBvJR7G8MmP5hUTje2mt20ClWS66nDvX0p-PeMm9RzuI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the i-th row of the file specifying the i-th entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are *distinct* numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example, you could compare performance under the chaining and open addressing approaches to resolving collisions.

大概的意思就是，计算里面出了-10000到10000这20001个数中的几个数s

```

```

---

**Test case:** [This file](http://www.algorithmsilluminated.org/datasets/problem12.4test.txt) describes an array with 9 integers. For how many target values t in the interval [3,10] are there distinct numbers x,y in the input array such that x+y=t? (Note: ensuring distinctness requires a one-line addition to the algorithm in Section 12.2.2.) (Answer: 8)