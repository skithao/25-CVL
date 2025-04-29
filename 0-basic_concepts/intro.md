# 基础概念认知
这一部分因为时间和内容特性原因建议穿插到其他三部分知识的学习过程中，目前规划的学习内容包括：
## 了解开源社区：
- git部署及github的使用流程（有时间可以加一些CI/CD的内容）
  - [git官网](https://git-scm.com/)
    ```bash
    # ubuntu配置git及gitlfs

    sudo apt-get update && sudo apt-get install git git-lfs -y

    # 验证git是否配置成功
    git -v
    ```
  - [github官网](https://github.com/)
  - [github简单操作](https://www.runoob.com/git/git-basic-operations.html)（其实vscode里的Git插件也蛮好用的）
- huggingface注册及使用（以如何[下载部署DeepSeek](0-basic_concepts/LocalDeepSeek/LocalDeepSeek.md)为例，大概了解下safetensor等权重文件的概念和各类LLM配置参数即可）
  - [huggingface官网](huggingface.co)
  - [huggingface使用技巧](https://blog.csdn.net/qq_61829672/article/details/143195653)(简单看眼，实操的时候有出入，能跑通DeepSeek应该就差不多)
- 常见的开源数据集平台使用
  - [OpenDataLab](https://opendatalab.com/)：国产数据集平台

## 了解深度学习相关方向的常见编程环境
- Linux系统
- [基础bash命令的使用](https://www.freecodecamp.org/chinese/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/)
- [miniconda的部署](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions)
- VScode及jupyter的使用

## 格式化文档编撰
- [markdown官方教程](https://markdown.com.cn/)

## 了解深度学习的前沿研究现状
- [arxiv](https://arxiv.org/)：常用的论文平台，可以通过[RSS](https://arxiv.org/rss/cs.LG.xml)订阅。
- [PaperWithCode](https://paperswithcode.com/sota)：好用的论文代码整合平台，方便复现论文。
- [机器之心](https://www.jiqizhixin.com/)