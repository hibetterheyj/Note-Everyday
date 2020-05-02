## Programming Assignment #3

1.Question 1

Download the following text file:

[Median.txt](https://d18ky98rnyall9.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_Median.txt?Expires=1588377600&Signature=T7~0aIqCiXODlVM-FTQvhWdOr5Do-GuOuO~~n~G9IKzmOtUhwYG56BogUItxA37UWIVcg47eg4w43RuqPM5cZPuUqrti0BBzGgAp3bpqxuBQjCvrEan-WjfvxHQMomWHPLGE0Bk-HPeV816epCK7w7Xmcis5Q9JlchWYEsjiyLI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting x_i denote the i-th number of the file, the *k*-th median m*k* is defined as the median of the numbers x*1*,..,x*k*. (So, if *k* is odd, then m*k* is ((k+1)/2)-th smallest number among x*1*,..,x*k*; if kis even, then m*k* is the (k/2)-th **smallest number** among x*1*,..,x*k*.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute **(*m*1+*m*2+*m*3+⋯+*m*10000) mod 10000**.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.

```

```

