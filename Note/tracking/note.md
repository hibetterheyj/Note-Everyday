# Tracking

### MBMD: Zhang2018arxiv

>  跟踪方法类文章
>  Zhang Y., et al. Learning regression and verification networks for long-term visual tracking. arxiv.

#### 解决问题：

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