# Medical image processing

### MBMD: Litjens2017Med_Image_Anal

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

#### 实验：

tracker achieves the best performance on the **VOT2018 long-term challenge** and state-of-the-art results on the **OxUvA long-term dataset**