# Event cameras

### Event-based Vision: A Survey: Gallego2019arxiv

> 综述类文章

#### Introduction and applicantions

- 总览：相比于传统相机，事件相机对于编码视觉信息产生了一种新的范式转变：Event cameras are asynchronous sensors that **pose a paradigm shift** in the way visual information is acquired.

- 优势：高时序分辨率，低延迟，高动态范围与低功率消耗Their advantages are: very **high temporal resolution** and **low latency** (both in the order of microseconds), very **high dynamic range** (140dB vs. 60dB of standard cameras), and **low power consumption**.

- 挑战：相比于传统方法，需要对于事件相机所产生的异步时间进行直接处理Because event cameras work in a fundamentally different way from standard cameras, measuring per-pixel brightness changes (called “events”) asynchronously rather than measuring “ab- solute” brightness at constant rate, novel methods are re- quired to process their output and unlock their potential

- 主要应用：**real-time** interaction systems, such as **robotics** or **wearable electronics**, where **operation under uncontrolled lighting conditions, latency, and power** are important

  Event cameras are used for object tracking, surveillance and monitoring, and object/gesture recognition, depth estimation, structured light 3D scanning, optical flow estimation, HDR image reconstruction, and Simultaneous Localization and Mapping (SLAM). 

  Event-based vision is a growing field of research, and other applications, such as image deblurring or star tracking,

- 论文结构：事件相机工作原理（2）；事件信息处理方法（3）；应用（4）；处理器与嵌入式系统（5）；相关软件，数据集与仿真环境（6）；探讨与结论（7，8）

  Section 2 presents event cameras, their working principle and advantages, and the challenges that they pose as novel vision sensors. 

  Section 3 discusses several methodologies commonly used to extract information from the event cam- era output, and discusses the biological inspiration behind some of the approaches. 

  Section 4 reviews applications of event cameras, from low-level to high-level vision tasks, and some of the algorithms that have been designed to unlock their potential. 

  Section 5 presents neuromorphic processors and embedded systems. 

  Section 6 reviews the software, datasets and simulators to work on event cameras, as well as additional sources of information.

  The paper ends with a discussion (Section 7) and conclusions (Section 8).

#### Principle of operation of event cameras

- 特点：Event cameras, such as the Dynamic Vision Sensor (DVS), **respond to brightness changes** in the scene **asynchronously and independently for every pixel**
- 灵感来源：the output of an event camera is a variable data-rate sequence of digital “events” or “spikes”. This encoding is inspired by the **spiking nature of biological visual pathways**
- 工作流程：
  - Each pixel **memorizes the log intensity** each time it sends an event, and **continuously monitors for a change** of sufficient magnitude **from this memorized value** (Fig. 1a). When the change **exceeds a threshold**, the camera sends an event, which is transmitted from the chip with the x, y **location**, the **time** t, and the 1-bit **polarity** p of the change for the denotation of brightness increase (“ON”) or decrease (“OFF”).
  - The events are transmitted from the pixel array to periphery and then out of the camera typically using **address-event representation (AER) readout**
  - Events are **timestamped** with **microsecond resolution** and are transmitted **with sub-millisecond latency**, which make these sensors **react quickly to visual stimuli.**
- 有点：These **changes in reflectance** are mainly **the result of the movement of objects** in the field. That is why the DVS brightness change events have a **built-in invariance to scene illumination** 

**2.1 Event Camera Designs**

The first silicon retina was developed during the period 1986-1992. After that, the DVS event camera, the Asynchronous Time Based Image Sensor (ATIS), and widely-used Dynamic and Active Pixel Vision Sensor
(DAVIS) are developed to generate the binary-polarity event output.

**2.2 Advantages of Event cameras**

- High Temporal Resolution: the read-out of the events is digital, so that events are **detected and timestamped with microsecond resolution**. Event cameras can capture very fast motions, **without suffering from motion blur typical of frame-based cameras**.
- Low Latency: each pixel works independently and there is **no need to wait for a global exposure time** of the frame. The cameras have minimal latency: about 10µs on the lab bench, and sub-millisecond in the real world.
- Low power: event cameras **transmit only brightness changes**, and thus remove redundant data, power is only used to process changing pixels.
- High Dynamic Range (HDR): event cameras can **acquire information from moonlight to daylight**. due to the facts that the photoreceptors of the pixels operate in logarithmic scale and each pixel works independently, **not waiting for a global shutter (快门)**. Like biological retinas, DVS pixels can **adapt to both dark and bright stimuli.**

**2.3 Challenges Due To The Novel Sensing Paradigm**

+ 不同寻常的时空输出：different space-time output: events are asynchronous and spatially sparse while images are synchronous and dense.
+ 不同寻常的光感知：different photometric sensing: Brightness changes depend **not only on the scene brightness**, but also on the current and past **motion between the scene and the camera**.
+ 噪音与动态效应：noise and dynamic effects: camera. 3) Coping with noise and dynamic effects: All vision sensors
  are noisy because of the inherent shot noise in photons
  3) Coping with noise and dynamic effects: All vision sensors are noisy. Additionally, the process of **quantizing temporal contrast is complex** and has not been completely characterized.

new methods need to rethink the **space-time**, **photometric** and **stochastic nature** of event data.

**3.3 Biologically Inspired Visual Processing**

Biological principles and computational primitives drive the design of event camera pixels and some of the event-processing algorithms (and hardware), such as Spiking N**eural Networks (SNNs).**

- 视觉通路Visual pathways: 

  The DVS [2] was inspired by the function of biological visual pathways, which have “tran- sient” pathways dedicated to processing dynamic visual information in the so-called “where” pathway

- 基于脉冲神经网络的事件处理Event processing by SNNs: 

  A neuron receives input spikes (“events”) from a small region of the visual space (a receptive field), which modify its internal state (membrane potential) and produce an output spike (action potential) when the state surpasses a threshold. Neurons are connected in a hierarchical way, forming an SNN. Spikes may be produced by pixels of the event camera or by neurons of the SNN. 

  The result of this visual processing is almost **simultaneous with the stimulus presentation** [152], which is very different from traditional CNNs, where convolution is computed simulta- neously at all locations at fixed time intervals.

---

### Template: NAME: {authoname}+{year}+{conference/journal}

> 架构/综述类文章
> {引用格式}

#### 面临问题：

#### 解决方法：

#### 实验：

