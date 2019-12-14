# Tracking

### MBMD: Zhang2018arxiv

>  跟踪方法类文章
>  Zhang Y., et al. Learning regression and verification networks for long-term visual tracking. arxiv.

#### 现有问题：

Compared with short-term tracking, the long-term tracking task requires **determining the tracked object is present or absent**, and then estimating the accurate bounding box if present or **conducting image-wide re-detection if absent**.

现有短时跟踪在数据集上已经取得很大的进步，但是仍然缺乏对于常识跟踪的有效评估。长时跟踪需要对于相比短时跟踪，还需判断出目标是否OV或者FOC，然后进行重检测。

First, the frame length in long- term benchmarks is almost ten times longer than that in short-term benchmarks. In addition, there exist a large amount of absent labels in long-term tracking scenarios.

长时跟踪特点：

1. 序列长度是短时跟踪序列十倍以上
2. 存在大量的absent labels

现有方法因为几个方面的原因，效果很不理想：1）使用local search策略，无法在目标消失后进行全局检索；2）跟踪模型不鲁棒/使用手工特征

#### 解决方法：

- The regression network is trained offline and fixed online for effective candidate proposal and reliable similarity estimation without accumulating errors in long sequences. 
- regression 网络使用不同参数分别对于example与当前搜索域进行多尺度（10x10与19x19）编码，然后进行 object-aware fusion（显示进行对template进行尺度扩充，然后对应元素点击的结果与扩充结果进行围堵上的拼接），最后送入region proposal的网络进行candidate的选取。
- regression 网络使用SSD的损失函数和MobileNet的架构，并且在跟踪过程中固定参数。
- The verification network is exploited to evaluate the generated candidates and fine-tuned online to capture the appearance variations. 
- 引入类似MDNet的网络架构对候选bb进行评估，并且动态更新最后三层卷积层，从而能应对跟踪过程动态变化的背景（tackle with various cluttered background during tracking.）
- verification 网络使用类似MDNet，属于在ImageNet上预训练的VGG-M网络，在跟踪过程动态更新。
- A dynamic switch scheme between local search and image-wide re-detection is designed based on a confidence score that is determined by the out- puts from both regression and verification networks. The

#### 实验：

tracker achieves the best performance on the **VOT2018 long-term challenge** and state-of-the-art results on the **OxUvA long-term dataset**

在VOT-2018 LTB35与OxUvA分别进行实验分析，分别试用了一下用于长时跟踪比较特别的分析指标（来自OxUvA）。使用LTB35进行了消融实验，证明原方法的有效性。

### CFNet: Valmadre17CVPR

> Valmadre J., et al. End-to-end representation learning for Correlation Filter based tracking

#### 现有问题：

- 尽管深度学习在视觉任务上取得重要表现，但是由于目标跟踪人物的特殊性，仅有第一帧为准确的先验信息，因此对于分类会造成很大的困难（lack of a-priori knowledge of the target ob- ject, which can be of any class）

- 一种解决方案是采用在线结合SGD进行参数更新，但是因为训练样本少+SGD更新速度慢不适用少样本，试试更新的场景
- 另外一种解决方案就是直接采用不在线更新的网络作为编码目标的描述子，但是相对固定的metric无法应对多变的环境
- 还有一种方法就是结合现有轻量化的CF框架，通过特别的性质实现在频域求解岭回归问题，以实现判别器的动态更新
- 因此引出已有的方法仅仅是在CF框架下简单利用CNN特征，而本文希望通过将CF作为内嵌的一个层来同时实现较为高效的在线学习和CNN特征高判别力的特征。

#### 解决方法：

- 原有Siamese网络架构是直接采用特征表达之后项目循环相关得到最大值来进行响应最高值的判定，训练过程则是输入样本x，较大搜索与z‘，然后结合pixel-wise的logistics二分类进行训练

$g_{\rho}\left(x^{\prime}, z^{\prime}\right)=f_{\rho}\left(x^{\prime}\right) \star f_{\rho}\left(z^{\prime}\right)$

- 现有方法则是希望结合CF架构，然后求解除滤波器w，在得到最终的响应

$h_{\rho, s, b}\left(x^{\prime}, z^{\prime}\right)=s \omega\left(f_{\rho}\left(x^{\prime}\right)\right) \star f_{\rho}\left(z^{\prime}\right)+b$

- 3.4 节即对于求解目标函数的过程

`具体过程待补充`

#### 实验：

最后在OTB与VOT上进行实验，相比于SiamFC有很大的表现提升。