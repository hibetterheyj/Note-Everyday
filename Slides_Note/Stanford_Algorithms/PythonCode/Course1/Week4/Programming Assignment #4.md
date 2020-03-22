## Programming Assignment #4

**TOTAL POINTS 1**

1.Question 1

Download the following text file:

[kargerMinCut.txt](https://d18ky98rnyall9.cloudfront.net/_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt?Expires=1584921600&Signature=hDZN~~EfIP-xgM8266fT5WEmS9Ood~rxZ9GXvuyXzeX773E6UiRhZMz11U0ytjTBqxgwsQYC7Cx1NYXrlPIAW3Oo6RkMYThHarvDu9VAr~-hYo3Z0GC~~u8XYa~hCaFdoVhpe4im0ENsDJ7tbcyWJ9~l~2gU2u0OX4DyR~JQ7k0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

The file contains the adjacency list representation of **a simple undirected graph**. There are **200 vertices labeled 1 to 200**. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6$^{th}$ row looks like : "6 155 56 52 120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and **run the randomized contraction algorithm** for the min cut problem and use it on the above graph to **compute the min cut**. (HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.

```

```

