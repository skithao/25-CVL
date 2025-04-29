# 236班计算机视觉及人工智能学习小组学习路径规划初版

## 目录
- [学习路径概述](##学习路径概述)
  - [查看基础介绍](./0-basic_concepts/intro.md)
  - [常见算法实现](./1-common_aigorithms/intro.md)
  - [arxiv论文分析](./2-arxiv_paper/intro.md)
  - [计算机视觉实战](./3-CV_project/intro.md)
- [学习资料推荐](#学习资料推荐)
  - 知识体系
  - 语言&工具

## 学习路径概述
我们的学习目前规划为三个月左右，主要分为以下几个部分：

### [基础介绍](./0-basic_concepts/intro.md)：
了解一些基本概念，这一部分因为时间和内容特性原因建议穿插到其他三部分知识的学习过程中，目前规划的学习内容包括：
#### 了解开源社区：
- git部署及github的使用流程（有时间可以加一些CI/CD的内容）
- huggingface注册及使用（以如何[下载部署DeepSeek](0-basic_concepts/LocalDeepSeek/LocalDeepSeek.md)为例，大概了解下safetensor等权重文件的概念和各类LLM配置参数即可）
#### 了解深度学习相关方向的常见编程环境
- Linux系统
- 基础bash命令的使用
- miniconda的部署
- VScode及jupyter的使用
#### 格式化文档编撰
- [markdown官方教程](https://markdown.com.cn/)

#### 了解深度学习的前沿研究现状
- [arxiv](https://arxiv.org/)：常用的论文平台，可以通过[RSS](https://arxiv.org/rss/cs.LG.xml)订阅。
- [PaperWithCode](https://paperswithcode.com/sota)：好用的论文代码整合平台，方便复现论文。
- [机器之心](https://www.jiqizhixin.com/)：深度学习相关论坛，提供顶会论文解读。

### [常见算法实现](./1-common_aigorithms/intro.md)：
学习和复现常见基础算法的实现方式，例如CNN、RNN等，并且引入一些计算机视觉的相关算法，包括R-CNN、语义分割等。
### [arxiv论文分析](./2-arxiv_paper/intro.md)：
学习一些经典文章和计算机视觉领域的最新研究成果，包括[Attention Is All You Need](https://arxiv.org/abs/1706.03762)(注意力机制)、[You Only Look Once](https://arxiv.org/abs/1506.02640)(YOLO)等。
### [计算机视觉实战](./3-CV_project/intro.md)：
通过实践来巩固所学知识，目前计划使用YOLO完成一些简单的计算机视觉项目。

## 学习资料推荐
### 知识体系
- [鸢尾花书](https://github.com/Visualize-ML)：基础的入门介绍，非常全但过于详细，适合作为手册查找。
- [pytorch官方手册](https://pytorch.org/docs/stable/nn.html)：我这边放的链接直接指向pytorch的nn部分功能的实现方式，可以看下这些常用工具的数学公式（某些论文里的公式基本基于就是这些进行一些调优）。
- [DeepML](https://www.deep-ml.com/)：一些基础代码的练习平台。

### 语言&工具
- [鸟哥的Linux私房菜](https://wizardforcel.gitbooks.io/vbird-linux-basic-4e/content/1.html)：没必要太详细看，遇到奇怪问题在这里找精确的问题描述然后问AI解决就行。
- [WSL2手册](https://learn.microsoft.com/zh-cn/windows/wsl/)：微软官方手册，上面的wsl部署内容还蛮方便的，其他的查手册即可。
- [菜鸟教程python3手册](https://www.runoob.com/python3/python3-tutorial.html)：感觉不用学特别细节的，语法部分可以交给AI努力（
- 
### 项目&模型
- [DeepSeek-R1的deepwiki页面](https://deepwiki.com/deepseek-ai/DeepSeek-R1):
- [YOLOv5的deepwiki页面](https://deepwiki.com/ultralytics/yolov5)
- [YOLIv10的deepwiki页面](https://deepwiki.com/THU-MIG/yolov10)
- [大佬的学习笔记](https://github.com/Phoenix-Shen)：本项目有很多笔记参考了这个项目，感谢开源。

### 免费云算力平台
- [Kaggle Notebooke](https://www.kaggle.com/code)：每周30小时免费算力。
- [Colab](https://colab.research.google.com/)：免费 GPU 资源，不过有时候等待时间有点长（