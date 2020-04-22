## Programming Assignment #1

1.Question 1

Download the following text file:

[SCC.txt](https://d18ky98rnyall9.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1587513600&Signature=ZWm~9NQ7f8IdIwXYteNOVE936Z225SekJgRql-FAFVC43cj44hSoUG13RBkj2qC0YamSUVoyOea0zd5VOuN1r6EyuR5G82zaywDPUh0FlYl8j3XOmsHF1uKvCuICNQRbyBla7TNwfvep-M1ObtLVJQqhe62OKXyhdXf1hmlOv48_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and **the edges are directed from the first column vertex to the second column vertex**). So for example, the $11^{th}$ row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing **strongly connected components (SCCs)**, and to run this algorithm on the given graph.

Output Format: You should output **the sizes of the 5 largest SCCs** in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.

```
434821,968,459,313,211
```

---

> Programming Problem 8.10: Computing Strongly Connected Components from https://www.algorithmsilluminated.org/

**Test case #1:** [A 9-vertex 11-edge graph.](https://www.algorithmsilluminated.org/datasets/problem8.10test1.txt) Top 5 SCC sizes: 3,3,3,0,0

**Test case #2:** [An 8-vertex 14-edge graph.](https://www.algorithmsilluminated.org/datasets/problem8.10test2.txt) Top 5 SCC sizes: 3,3,2,0,0

**Test case #3:** [An 8-vertex 9-edge graph.](https://www.algorithmsilluminated.org/datasets/problem8.10test3.txt) Top 5 SCC sizes: 3,3,1,1,0

**Test case #4:** [An 8-vertex 11-edge graph.](https://www.algorithmsilluminated.org/datasets/problem8.10test4.txt) Top 5 SCC sizes: 7,1,0,0,0

**Test case #5:** [A 12-vertex 20-edge graph.](https://www.algorithmsilluminated.org/datasets/problem8.10test5.txt) Top 5 SCC sizes: 6,3,2,1,0

**Challenge data set:** [This file](https://www.algorithmsilluminated.org/datasets/problem8.10.txt) describes the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Each row indicates one edge of the graph (the tail and head vertices, in that order). For example, the eleventh row ("2 13019") indicates that there is an edge directed from vertex 2 to vertex 13019. What are the sizes of the biggest five strongly connected components?