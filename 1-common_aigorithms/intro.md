# 常见算法复现

## 📂 项目结构
```
.
├── 0-basic_concepts             # 基础概念
├── 1-common_aigorithms          # 经典算法实现
│ ├── 0-BasicMath             # 基础数学知识
│ ├── 1-NeuralNetworkBasics      # 神经网络基础
│ │ ├── 01-LinearNeuralNetwork    # 前馈神经网络
│ │ ├── 02-MultilayerPerceptron     # 多层感知机
│ │ ├── 03-ConvolutionalNeuralNetwork # 卷积神经网络
│ │ ├── 04-RecurrentNeuralNetwork   # 循环神经网络
│ │ ├── 05-LongShort-TermMemory    # 长短期记忆网络
│ │ └── 06-GatedRecurrentUnit     # 门控循环单元
│ ├── 2-OptimizationAlgorithms       # 优化算法
│ │ ├── 01-GradientDescent        # 梯度下降
│ │ ├── 02-StochasticGradientDescent  # 随机梯度下降
│ │ ├── 03-MomentumMethod         # 动量法
│ │ ├── 04-AdamOptimizer         # 自适应优化
│ │ └── 05-OtherOptimizationAlgorithms # 多样优化法
│ ├── 3-ModernArchitectures         # 现代架构
│ │ ├── 01-ModernCNN            # 卷积神经网络改进
│ │ └── 02-ModernRNN            # 循环神经网络改进
│ │ ├── 03-AttentionMechanism       # 自注意力机制
│ ├── 4-Open-SourceFrameworksAndTools  # 开源框架与工具
│ │ ├── 01-OpenCV               # 传统视觉工具
│ │ └── 02-PyTorch               # 深度学习框架
│ ├── 5-GenerativeModels           # 生成模型
│ │ ├── 01-GenerativeAdversarialNetwork  # 生成对抗网络
│ │ ├── 02-VariationalAutoencoder      # 变分自编码器
│ │ ├── 03-DeepConvolutionalGAN      # 深度卷积 GAN
│ │ ├── 04-WassersteinGAN          # 稳定生成质量
│ │ ├── 05-YOLO                # 目标检测算法
│ │ ├── 06-FasterR-CNN           # 区域提议检测
│ │ ├── 07-MaskR-CNN            # 实例分割模型
│ │ └── 08-SegNet&U-Net          # 语义分割模型
│ ├── 6-ModelDeploymentAndOptimization  # 模型部署与优化
│ │ ├── 01-ModelQuantization        # 降低模型精度
│ │ ├── 02-ModelPruning           # 去除冗余连接
│ │ ├── 03-TensorRT              # 加速推理计算
│ │ ├── 04-ONNX                # 网络交换格式
│ │ └── 05-SafeTensor             # 模型存储格式
│ └── 7-Cutting-EdgeTechnologies       # 前沿技术
│   ├── 01-Diffusion            # 扩散模型技术
│   ├── 02-CLIP                # 语言图像预训
│   ├── 03-DALL-E               # 文本图像生成
│   ├── 04-MetaLearning           # 元学习
│   ├── 05-Self-SupervisedLearning     # 自监督学习
│   └── 06-Zero-ShotLearning        # 零样本学习
├── 2-arxiv_paper                # 前沿论文复现
└── 3-CV_project                 # 简单的完整项目实践
```