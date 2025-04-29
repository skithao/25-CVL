# exercises/image_processing.py
"""
练习：图像基本处理

描述：
使用 OpenCV 实现基本的图像读取、灰度转换、高斯滤波和边缘检测。

请补全下面的函数 `image_processing_pipeline`。
"""
import cv2
import numpy as np

def image_processing_pipeline(image_path):
    """
    使用 OpenCV 读取图像，进行高斯滤波和边缘检测。
    参数:
        image_path: 图像文件的路径 (字符串).
    返回:
        edges: Canny 边缘检测的结果 (NumPy 数组, 灰度图像).
               如果读取图像失败, 返回 None.
    """
    # 请在此处编写代码
    # 提示：
    # 1. 使用 cv2.imread() 读取图像。
    # 2. 检查图像是否成功读取（img is None?）。
    # 3. 使用 cv2.cvtColor() 将图像转为灰度图 (cv2.COLOR_BGR2GRAY)。
    # 4. 使用 cv2.GaussianBlur() 进行高斯滤波。
    # 5. 使用 cv2.Canny() 进行边缘检测。
    # 6. 使用 try...except 包裹代码以处理可能的异常。
    try:
        img = cv2.imread(image_path)
        if img is None:
            return None
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 100, 200)
        return edges
    except:
        return None
    pass 