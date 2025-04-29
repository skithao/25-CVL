# DeepSeek 对话系统

一个基于DeepSeek-R1-Distill-Qwen-1.5B模型的对话系统，提供流式交互的聊天体验。

## 系统要求

- Ubuntu 20.04LTS 以上
- NVIDIA GPU (至少16GB显存)
- 至少20GB可用磁盘空间

## 安装指南

### 1. 基础环境配置

#### 安装Conda

```bash
# 下载Miniconda安装脚本
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 运行安装脚本
bash Miniconda3-latest-Linux-x86_64.sh

# 按照提示完成安装后，关闭并重新打开终端
# 验证安装
conda --version

# 创建虚拟环境
conda create -n deepseek python=3.8

# 激活虚拟环境
conda activate deepseek
```

#### 安装Docker
```bash
sudo apt update
sudo apt install docker.io docker-compose-plugin
sudo systemctl enable --now docker
```
或者复杂点的
```bash
# 安装依赖
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg -y

# 添加Docker阿里云源GPG密钥
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# 设置仓库
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

---
# 添加NVIDIA Docker仓库
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
---

# 更新软件包索引
sudo apt-get update

# 安装Docker引擎和nvidia-container-toolkit
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# 开启Docker服务
sudo systemctl start docker

# 确认Docker服务已开启
sudo systemctl status docker

# 验证安装
sudo docker pull hello-world
sudo docker run hello-world
```

#### 安装CUDA

```bash
# 安装CUDA工具包
sudo apt-get install nvidia-cuda-toolkit -y

# 验证安装
nvidia-smi
nvcc --version
```

### 2. 项目设置

#### 克隆项目（暂时没放到github上）

```bash
git clone <项目仓库地址>
cd <项目目录>
```

#### 准备模型

下载DeepSeek-R1-Distill-Qwen-1.5B模型![](https://hf-mirror.com/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B/tree/main)
```bash
# 配置Git LFS
sudo apt-get install git-lfs -y

# 从镜像网站下载模型文件
git lfs clone https://hf-mirror.com/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
```

### 3. 运行项目

#### 使用Docker运行（推荐）

```bash
# 配置Docker-compose
sudo apt-get install docker-compose -y

# 在本项目的根目录构建并启动服务(可以通过配置用户组避免使用sudo)
sudo docker-compose up -d

# 查看服务状态
sudo docker-compose ps

# 停止服务
sudo docker-compose down
```

服务启动后：
- 模型API服务: http://localhost:8000
- 对话后端服务: http://localhost:5000

#### 原生方式运行

1. 启动模型服务:

```bash
bash start.sh
```

2. 启动对话后端:

```bash
python backend.py
```

### 使用说明

1. 启动后会显示交互式对话界面
2. 输入您的问题或对话内容
3. 特殊命令:
   - `reset`: 清空对话历史
   - `exit`: 退出程序

## 注意事项

1. 首次运行需要下载vLLM镜像，可能需要较长时间
2. 确保模型文件路径正确
3. 如果遇到GPU内存不足错误，尝试:
   - 减小`max_tokens`参数
   - 使用更小的模型
4. 确保Docker有权限访问GPU:
   ```bash
   sudo groupadd docker
   sudo usermod -aG docker $USER
   newgrp docker
   ```

## 常见问题

**Q: 遇到CUDA错误怎么办?**
A: 确保安装了正确版本的NVIDIA驱动和CUDA工具包

**Q: Docker容器无法启动?**
A: 检查日志:
```bash
docker-compose logs
```

**Q: 模型响应速度慢?**
A: 尝试减小`max_tokens`参数值