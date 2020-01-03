## Deep learning

[toc]

### MobileNetV1: Howard2017arxiv

> 架构类文章
> Howard A., et al. MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications, arxiv 2017

#### 面临问题：

提出了一种适用于移动端地神经网络架构，并且引入两个超参数用于实现在时间延迟与准确率上的权衡

#### 解决方法：

- 相比使用缩小/分解/压缩已有网络或者使用知识蒸馏（使用大型网络协助训练小网络）的方达，本文借鉴了在Inception中所使用的 depthwise separable convolutions，提出一种全新的架构进行小网络训练。
- 主要包括depth-wise卷积（对应PyTorch中`nn.Conv2d`中`groups=input_channels`的概念）以及1x1的point-wise卷积操作进行组合8

- 参数量对比，由于主要使用1x1的卷积代替之前一步的3x3卷积，总体参数计算量约为原来的1/8~1/9：

$\dfrac{D_{K} \cdot D_{K} \cdot M \cdot D_{F} \cdot D_{F}+M \cdot N \cdot D_{F} \cdot D_{F}}{D_{K} \cdot D_{K} \cdot M \cdot N \cdot D_{F} \cdot D_{F}}=\dfrac{1}{N}+\dfrac{1}{D_{K}^{2}}$

- 引入宽度乘子$ \alpha $来实现更窄的网络以进行维度的压缩
- 引入分辨率乘子$ \rho $来实现更窄的网络以进行输入图像分辨率缩减

#### 实验：

- 自身实验：与常规卷积，浅层网络，以及不同大小的宽度/分辨率因子进行充分实验，证明采用更瘦的网络可以比更浅的网络取得更好的效果（making MobileNets thinner is 3% better than making them shallower.）
- 数据集实验：在几个应用数据集/网络架构上进一步测试：Fine Grained Recognition——Stanford Dogs dataset，Large Scale Geolocalizaton——PlaNet，Object Detection——COCO object detection，Face Embeddings——FaceNet

---

### MobileNetV2: Sandler2018CVPR

> 架构类文章
> Sandler M., et al. MobileNetV2: Inverted Residuals and Linear Bottlenecks, CVPR 2018

#### 面临问题：

- 进一步拓展MobileNetV1
- 实验发现，过多使用ReLU激活函数引入的非线性可能造成对已有信息的破坏。Experimental evidence suggests that using linear layers is crucial as it prevents non-linearities from destroying too much information.

#### 解决方法：

- 提出新的模块：the inverted residual with linear bottleneck
- 在模块的输出层将传统的ReLU层取消掉，直接线性输出，理由是：ReLU变换后保留非0区域对应于一个线性变换，仅当输入低维时ReLU能保留所有完整信息。
- 利用了res模块，但是与以往不同中间降低维度操作的是，inverted residual中间层结合扩增因子（t, expansion ratio）去更好捕获物体信息，并且可以实现精度与计算量的权衡

#### 实验：

除了进行ablation studies，还针对检测和分割数据集进行后续的修改，在ImageNet, classification, COCO object detection, VOCimage segmentation数据集进行实验分析。

---

### MobileNetV3: Howard2019arxiv

> 架构类文章
> Howard A., et al. Searching for MobileNetV3, arxiv 2019

#### 面临问题：

- 希望进一步部署到移动平台上，以及尽可能更好的进行精度和时间延迟上的权衡

- 近年来NAS，神经网络架构搜索将能够进一步提高神经网络地性能，如基于MnasNet是基于MobileNetV2进行的NAS

#### 解决方法：

- 将DW, PW. inverted residual, SE等作为基本block进行NAS

- 重新设计网络头尾开销巨大地部分（We redesign the computionally-expensive layers at the beginning and the end of the network. ）

  - 经过搜索与验证，简化网络最后部分，移除原有the projection and filtering layers in the previous bottleneck layer
  - 经过搜索，使用16个卷积核代替了原有32个（We were able to reduce the number of filters to 16 while main- taining the same accuracy as 32 filters using either ReLU or swish.）

- 结合现有swish非线性激活函数，并进一步优化为hard swish函数，在整体架构的后半部分使用（We also introduce a new nonlinearity, h-swish, a modified version of the recent swish nonlinearity, which is faster to compute and more quantization-friendly）

  - 原有swish使用sigmoid函数：

    $\mathrm{swish} x=x \cdot \sigma(x)$

  - 减少卡销，结合ReLU以及固定常数：

    $\mathrm{h}-\mathrm{swish}[x]=x \dfrac{\operatorname{ReLU} 6(x+3)}{6}$

#### 实验：

- 使用手机端进行测试
- 进行了分类/检测/分割任务的实验，并提出了新型分割decoders LR-ASPP

---

### Template: NAME: {authoname}+{year}+{conference/journal}

> 架构/综述类文章
> {引用格式}

#### 面临问题：

#### 解决方法：

#### 实验：

