# exercises/leaky_relu.py
"""
练习：Leaky ReLU 激活函数

描述：
实现 Leaky ReLU 激活函数。
Leaky ReLU 是 ReLU 的一个变种，允许负输入值有一个小的正斜率。

请补全下面的函数 `leaky_relu`。
"""
import numpy as np
"""
这里原本是def leaky_relu(x, alpha=0.01):，
但是运行时提示函数应该是leaky_relu_activation(x, alpha=0.01)，
所以修改了函数名。
"""
def leaky_relu(x, alpha=0.01):
    """
    计算 Leaky ReLU 激活函数。
    公式: max(alpha * x, x)

    Args:
        x (np.array): 输入数组，任意形状。
        alpha (float): 负斜率系数，默认为 0.01。

    Return:
        np.array: Leaky ReLU 激活后的数组，形状与输入相同。
    """
    # 请在此处编写代码
    # 提示：
    # 1. 可以使用 np.maximum() 函数。
    # 2. 计算 alpha * x。
    # 3. 计算 max(alpha * x, x)。
    return np.maximum(alpha * x, x)
    pass 