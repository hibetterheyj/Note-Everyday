##  Note for Lecture 1: Mathematical Background Linear Algebra

> **Multiple View Geometry** Given by  Prof. D. Cremers
>
> [YouTube Link](https://youtu.be/RDkwklFGMfo?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4) Click here!
>
> **Updating Log**
>
> 180510 is ended at [**Kronecker Product and Stack of a Matrix**](https://youtu.be/RDkwklFGMfo?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4&t=1752)
>
> To be continued.

###  Word List

```
vector spaces | 向量空间
scalar | 标量
linearly independent | 线性独立
Inner Product | 内积
Hilbert space | 希尔伯特空间
metric space | 度量空间
Taxicab geometry(Manhattan distance) | 曼哈顿距离
canonical | 正则
orthogonal | 正交
Kronecker Product | 克罗内克积
stack of a matrix | 矩阵向量化
```



###  Vector Spaces | 向量空间

####  Vector Space

> A set V is called a **linear space** or a **vector space over the field R** if it is closed under vector summation.

- Scalar multiplication and addition respects the distributive law

####  Linear Independence and Basis

- The linearly independent of a vector set means that each vector contributes something and they form a basis of Vector Space
- the number of vectors in a basis is called the **dimension of the space**
- Any vector in Vector Space can be uniquely expressed as a linear combination of the basis vectors.(can be proved by contradiction)
- A Vector Space can have different kinds of basis, the different bases can be transformed into each other by the matrix and its inverse
- **bases transformation can be applied into the relation between the moving camera and the world reference.**

####  Inner Product

> a scalar function of two vectors, equal to the product of their magnitudes and the cosine of the angle between them.
>
> Wikipedia - [Inner Product Space](https://www.wikiwand.com/en/Inner_product_space)

- Inner Product can be defined by three properties: **Linear**, **Symmetric** and **Positive definite**.
- Two terms: [Metric space](https://www.wikiwand.com/en/Metric_space) and [Manhattan distance](https://www.wikiwand.com/en/Manhattan_distance) 
- **Hilbert space** is a metric space which is induced by the scalar product.

####  Canonical and Induced Inner Product

> A little confusing [here](https://youtu.be/RDkwklFGMfo?list=PLTBdjV_4f-EJn6udZ34tht9EVIW7lbeo4&t=1532).

####  Kronecker Product and Stack of a Matrix

- a new concept called [Kronecker Product](https://www.wikiwand.com/en/Kronecker_product) which is different from inner or outer product.
- In Matlab this can be implemented by `C=kron(A,B)`
- These notations allow to rewrite algebraic expressions by the **Stack of a Matrix**

###  Linear Transformations and Matrices    



###  Properties of Matrices



###  Singular Value Decomposition






