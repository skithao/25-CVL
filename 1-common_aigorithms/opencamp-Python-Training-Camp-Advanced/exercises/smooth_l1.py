# exercises/smooth_l1.py
"""
练习：Smooth L1 损失函数

描述：
实现 Smooth L1 损失函数，常用于目标检测中的边界框回归。

请补全下面的函数 `smooth_l1`。
"""
import numpy as np
"""
这里原本是def smooth_l1(x, sigma=1.0)，
但是运行时提示函数应该是smooth_l1_loss(x, sigma=1.0)，
所以修改了函数名。
这边修改了下smooth_l1_loss函数的传参(测例里传了三个参：y_pred, y_true, beta，原题里只传了两个参：x, sigma = 1.0)
，用于允许test_cross_entropy.py正确测试。
"""
def smooth_l1(x, sigma = 1.0):
    """
    计算 Smooth L1 损失。
    公式:
        0.5 * (sigma * x)**2   if |x| < 1 / sigma**2
        |x| - 0.5 / sigma**2   otherwise

    Args:
        x (np.array): 输入差值数组，任意形状。
        sigma (float): 控制平滑区域的参数，默认为 1.0。

    Return:
        np.array: 计算得到的 Smooth L1 损失数组，形状与输入相同。
    """
    # 请在此处编写代码
    # 提示：
    # 1. 计算 sigma 的平方 sigma2。
    # 2. 找到满足条件 |x| < 1 / sigma2 的元素索引 (可以使用 np.abs 和比较运算符)。
    # 3. 对满足条件的元素应用第一个公式 (0.5 * (sigma * x)**2)。
    # 4. 对不满足条件的元素应用第二个公式 (|x| - 0.5 / sigma2)。
    # 5. 可以使用 np.where() 来根据条件选择应用哪个公式。
    sigma2 = sigma ** 2
    abs_x = np.abs(x)
    loss_array = np.where(abs_x < 1 / sigma2, 0.5 * (sigma * abs_x) ** 2, abs_x - 0.5 / sigma2)
    return np.mean(loss_array)
    pass 