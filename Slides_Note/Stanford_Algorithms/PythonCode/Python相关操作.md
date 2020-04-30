## Python相关操作

- 替换字符

    ```python
    tj = '1.0.0.0'
    #使无效化
    tj.replace('.', '$@!')
    '$@!'.join(tj.split('.'))
    ```

- 打开文件

  ```
  testFile = "problem9.8test.txt"
  challengeFile = "dijkstraData.txt"
  # 第一种写法
  #with open(r"problem9.8test.txt", "r") as f:
  #    data = f.readlines()
  # 第二种写法
  f=open(testFile,'r')
  data = f.readlines()
  ```

- 构建无向图

  ```
  def load_graph():
      return {int(line.rstrip().split()[0]): [int(i) for i in line.rstrip().split()[1:]] for line in
         open("./kargerMinCut.txt")}
  ```

  对应的`./kargerMinCut.txt`

  ```
  1	37	79	164	155	32
  2	123	134	10	141	13
  ```

  生成graph

  ```
  graph=
  {
  1: [37, 79, 164, 154, 34]
  2: [3123, 134, 10, 141, 13]
  }
  ```

- `rstrip()`与`strip()`

  1. rstrip 要删除的指定字符（默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等）
  2. strip() 相当于就是去掉字符串类种相似的字符，然后输出字符数组，**可以控制数量**（默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等）

- [Python 简化for循环：列表，集合与字典生成式](https://www.cnblogs.com/legoxz/p/8515308.html)

  **列表生成式**

  ```
  # 使用列表生成选择特定的行
  my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  rows_to_keep = [row for row in my_data if row[2] > 5]
  print("Output #1 (list comprehension): {}".format(rows_to_keep))
  ```

  列表生成式的意义是：对于my_data中的每一行，如果这行中索引位置2的值大于5，则保留这行。

  **集合生成式**

  ```
  #使用集合生成式在列表中选择出一组唯一的元组
  my_data = [(1, 2, 3), (4, 5 ,6), (7, 8, 9), (7, 8, 9)]
  set_of_tuples1 = {x for x in my_data}
  print("Output #2 (set comprehension): {}".format(set_of_tuples1))
  set_of_tuples2 = set(my_data)                  #内置的set函数更好
  print("Output #3 (set function): {}".format(set_of_tuples2))
  ```

  **字典生成式**

  ```
  #使用字典生成式选择特定的键-值对
  my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
  my_results = {key : value for key, value in my_dictionary.items() if value > 10}
  print("Output #3 (dictionary comprehension): {}".format(my_results))
  ```

   