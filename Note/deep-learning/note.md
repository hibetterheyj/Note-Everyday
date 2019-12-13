# Deep learning

### U-Net: Ronneberger2015MICCAI

>  架构类文章
>  Ronneberger et al. U-Net: Convolutional Networks for Biomedical Image Segmentation

#### 面临问题：

the success of CNN was limited due to the size of the **available training sets** and the size of the **considered networks.**

现有CNN的性能受限于数据集的大小以及网络架构的参数量

In many visual tasks, especially in biomedical image processing, the desired output should include localization, i.e., a class label is supposed to be assigned to each pixel.

对于除分类以外的视觉任务，如医学图像处理的定位任务，需要对于图片中的每个像素生成对应的标签。

a network in a sliding-window setup to predict the class label of each pixel by providing a local region (patch) around that pixel ... has two drawbacks.

已有在ISBI数据集上成功的方法仍然存在两个主要弊端：

1. 由于使用滑窗方法来预测像素的label，因此运算过程会有很多重复部分，数据冗余造成运行缓慢；
2. 在上下文使用和定位精度需要进行取舍

#### 解决方法：

- 采用了全卷积网络 fully convolutional network
- 使用 upsampling 取代pooling操作
- 并且结合contracting path，将下采样阶段的feature map与上采样后的进行维度上的拼接，以提高定位精度
- 并且使用 Overlap-tile strategy 用镜像样本，来用于后续分割
- 使用基于“弹性变形”的数据增广方法来生成训练样本 use excessive data augmentation by applying elastic deformations to the available training images
- 使用带有权重的损失函数，来进行相似物体的分离

---

- 训练阶段
  - 使用尽可能大的输入，因此将batch减少至一张图片 (favor large input tiles over a large batch size and hence reduce the batch to a single image)，并且使用momentum=0.99，用过去样本决定未来更新方向
  - 能量方程 = a pixel-wise soft-max + the cross entropy loss function
  - 预先计算权重图 weight map = 类出现频率 + 当前像素与最近两个细胞的靠近程度决定（靠近两细胞边界越近，权重越大）
  - 使用与层数和卷积核大小相关的参变量生成用于初始化的高斯分布 drawing the initial weights from a Gaussian distribution 
- 数据增广
  - 使用随机向量在3x3的网格内进行平滑变形操作，然后结合插值生成新样本 smooth deformations using random displacement vectors

#### 实验：

We demonstrate the application of the u-net to three different segmentation tasks, EM segmentation challenge, ISBI cell tracking challenge 2014 and 2015.

主要在三个数据集上进行测试，在速度和精度都取得很大进步。