# exercises/iou.py
"""
练习：计算交并比 (Intersection over Union, IoU)

描述：
实现用于计算两个边界框之间交并比 (IoU) 的函数。
IoU 是目标检测任务中常用的评估指标。

请补全下面的函数 `calculate_iou`。
"""
import numpy as np

def calculate_iou(box1, box2):
    """
    计算两个边界框 (bounding box) 的交并比 (IoU)。
    边界框格式：[x_min, y_min, x_max, y_max]

    Args:
        box1 (list or np.array): 第一个边界框的坐标 [x1_min, y1_min, x1_max, y1_max]。
        box2 (list or np.array): 第二个边界框的坐标 [x2_min, y2_min, x2_max, y2_max]。

    Return:
        float: 计算得到的 IoU 值，范围在 [0, 1]。
    """
    # 请在此处编写代码
    # 提示：
    # 1. 确定两个框相交区域的左上角坐标 (x_left, y_top)。
    #    x_left = max(box1[0], box2[0])
    #    y_top = max(box1[1], box2[1])
    # 2. 确定两个框相交区域的右下角坐标 (x_right, y_bottom)。
    #    x_right = min(box1[2], box2[2])
    #    y_bottom = min(box1[3], box2[3])
    # 3. 计算相交区域的面积 intersection_area。
    #    注意处理不相交的情况 (宽度或高度 <= 0)。
    #    intersection_area = max(0, x_right - x_left) * max(0, y_bottom - y_top)
    # 4. 计算 box1 的面积 box1_area。
    # 5. 计算 box2 的面积 box2_area。
    # 6. 计算并集面积 union_area = box1_area + box2_area - intersection_area。
    # 7. 计算 IoU = intersection_area / union_area。
    #    注意处理 union_area 为 0 的情况 (除零错误)。
    x_left = max(box1[0], box2[0])
    y_top = max(box1[1], box2[1])
    x_right = min(box1[2], box2[2])
    y_bottom = min(box1[3], box2[3])
    intersection_area = max(0, x_right - x_left) * max(0, y_bottom - y_top)
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union_area = box1_area + box2_area - intersection_area
    if union_area == 0:
        return 0
    else:
        return intersection_area / union_area
    pass 