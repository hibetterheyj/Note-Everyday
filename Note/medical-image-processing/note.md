# Medical image processing

### nnUNet_Isensee2018arxiv

#### 现有问题

- 现有基于U-Net的方法通关各种特别的结果和方法来实现在特定数据集上的优越性，而难以考据其效果的真实性。

- 现有方法可能是在特定数据集上发生过拟合，或者可能难以复现与验证。
- 神经网络架构，前处理，训练，因果推断以及后处理都是影响U-Net性能的关键因素，而其中non-architectual部分被较为严重的低估

#### 解决方法

- 摒弃最近在分割领域引入的 residual connections [7,8], dense connections [5] or attention mechanisms [4]
- 考虑架构的通用性和数据集几何性质，分别通过对于前处理的采样和正则化；训练的损失函数，优化器选择和数据增强；推断时的基于块的策略以及ensemble方法；以及后处理技术实现更加通用的框架。
- 网络架构，采取U-Net pool：包含2D, 3D以及3D级联网络，并且采用Leaky RELU损失函数以及instance normalization
- 前处理/Preprocessing：对于MRI数据的剪裁操作；对于体素信息的重采样于插值；对于CT图像根据数据集总体特性进行正则化以及对MRI的z-score正则；
- 训练/Training：采用dice+BCE loss；结合Adam优化器
- 数据增广/Data augmentation：代码可见<github.com/MIC-DKFZ/batchgenerators>.
- 推断/Interface：基于patch级别的预测，并使用五折交叉验证

- 后处理与实验

#### 实验

- 在Medical Segmentation Decathlon challenge，通过对于十种不同特性，模态，几何关系，以及数据集大小进行测试，在投稿时，实现了最高的效果和性能

---

### Litjens2017Med_Image_Anal

>  综述类文章
>  Litjens, G., et al. A survey on deep learning in medical image analysis. Medical Image Analysis, 2017.

#### 关注点：

*The motivation for our review was to offer a comprehensive overview of (almost) all fields in medical imaging, both from an application and a methodology driven perspective.*

对于目前应用于医疗图像处理基本任务的基本算法进行调研，并后续结合ROI（如neuro, retinal, pulmonary, digital pathology, breast, cardiac, abdominal, musculoskeletal）进行分类应用阐述

#### 解决方法：

1. Deep CNN architecture:
2. Segmentation architecture: U-Net [Ronneberger et al. (2015) ] -> U-Net for 3D data [Çiçek et al. (2016)] -> Res-block+Dice loss [Milletari et al. (2016b)]
3. RNN
4. Unsupervised models

#### 应用：

- 分类
  - Image/exam classificatio | 图像分类：数据非常小，因此transfer learning较为常见；使用pre-trained作为特征提取或是用于fine-tune，前者可以直接与现有方法整合，后者则是可以实现更好的效果
  - Object or lesion classificatio | 物体/病灶分类：主要关注整体图片中很小的区域，如胸部的肿块（nodule classification in chest CT）；主要使用multi-stream architectures，而少用pre-trained是因为需要周围的context信息以及需要处理3D数据
- 检测与定位
  - Organ, region and landmark localization | 器官/区域定位
  - Object or lesion detection | 物体/病灶检测
- 分割

#### 展望：

`未完待续`