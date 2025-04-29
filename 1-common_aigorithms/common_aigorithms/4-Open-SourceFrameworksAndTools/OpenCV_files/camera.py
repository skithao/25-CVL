import cv2
import numpy as np
from PIL import Image

# 打开摄像头
cap = cv2.VideoCapture(0)
# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 读取一帧图像
    ret, frame = cap.read()
    # 如果读取失败，退出循环
    if not ret:
        print("无法读取摄像头")
        break

    # 1. 预处理 - 灰度转换
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. 预处理 - 图像标准化
    # 计算图像的均值和标准差
    mean = np.mean(gray_frame)
    std = np.std(gray_frame)
    # 进行标准化
    std_frame = (gray_frame - mean) / std
    # 由于标准化后的像素值可能不在 [0, 255] 范围内，需要进行裁剪和类型转换
    std_frame = np.clip(std_frame, -1, 1)
    std_frame = ((std_frame + 1) / 2 * 255).astype(np.uint8)

    # 3. Canny 边缘检测
    edges = cv2.Canny(std_frame, 100, 200)

    # 4. 轮廓提取
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 5. 绘制轮廓
    contour_frame = frame.copy()
    cv2.drawContours(contour_frame, contours, -1, (0, 255, 0), 2)

    # 显示图像
    cv2.imshow('frame', contour_frame)
    # 等待按键事件，如果按下 'q' 键，退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()