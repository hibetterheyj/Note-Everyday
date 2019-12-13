# Medical image processing

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