# exercises/cross_entropy.py
"""
练习：交叉熵损失 (Cross Entropy Loss)

描述：
实现分类问题中常用的交叉熵损失函数。

请补全下面的函数 `cross_entropy_loss`。
"""
import numpy as np
"""
这边修改了下cross_entropy_loss函数的传参(测例里传参顺序与原函数相反)，用于允许test_cross_entropy.py正确测试。
"""
def cross_entropy_loss(y_true, y_pred):
    """
    计算交叉熵损失。

    Args:
        y_true (np.array): 真实标签 (独热编码或类别索引)。
                           如果 y_true 是类别索引, 它将被转换为独热编码。
                           形状: (N,) 或 (N, C)，N 是样本数, C 是类别数。
        y_pred (np.array): 模型预测概率，形状 (N, C)。
                           每个元素范围在 [0, 1]，每行的和应接近 1。

    Return:
        float: 平均交叉熵损失。
    """
    # 请在此处编写代码
    # 提示：
    # 1. 获取样本数量 N 和类别数量 C。
    # 2. 如果 y_true 是类别索引 (形状为 (N,)), 将其转换为独热编码 (形状为 (N, C))。
    #    (可以使用 np.eye(C)[y_true] 或类似方法)。
    # 3. 为防止 log(0) 错误，将 y_pred 中非常小的值替换为一个小的正数 (如 1e-12)，
    #    可以使用 np.clip(y_pred, 1e-12, 1.0)。
    # 4. 计算交叉熵损失：L = - sum(y_true * log(y_pred))。
    #    在 NumPy 中是 -np.sum(y_true * np.log(y_pred))。
    # 5. 计算所有样本的平均损失：L / N。
    N = y_pred.shape[0]
    C = y_pred.shape[1]

    if y_true.ndim == 1:
        y_true = np.eye(C)[y_true]

    y_pred = np.clip(y_pred, 1e-12, 1.0)

    loss = -np.sum(y_true * np.log(y_pred))

    return loss / N
    pass 