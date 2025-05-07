import cv2
import numpy as np

# 步骤0：准备阶段（模拟图中特征提取过程）
def extract_handcrafted_features(img):
    """模拟图片中描述的手工特征提取流程"""
    # 颜色特征（模拟黄色毛发统计）
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    yellow_mask = cv2.inRange(hsv, (20, 50, 50), (30, 255, 255))
    
    # 形状特征（HOG边缘检测）
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hog = cv2.HOGDescriptor()
    h = hog.compute(gray)
    
    # 纹理特征（LBP纹理分析）
    lbp = cv2.calcHist([gray], [0], None, [256], [0,256])
    
    return yellow_mask, h, lbp

# 步骤1：加载预训练模型（对应图中"Haar-like特征训练的小狗检测器"）
cascade_path = 'haarcascade_frontalface_default.xml'  # 需替换为实际的小狗检测器XML文件
dog_cascade = cv2.CascadeClassifier(cascade_path)

# 步骤2：特征检测与匹配（核心代码）
def detect_dogs(img):
    """实现detectMultiScale检测流程"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 参数说明（对应图中特征网络输出）：
    # scaleFactor=1.1 - 图像缩放步长（模拟特征金字塔）
    # minNeighbors=3  - 匹配阈值（模拟测量网络的匹配得分）
    # minSize=(30,30) - 最小检测窗口（模拟滑动窗口尺寸）
    dogs = dog_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1,
        minNeighbors=3, 
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    return dogs

# 步骤3：结果可视化（严格按图片说明实现）
def visualize_detection(img, dogs):
    """实现rectangle和putText标注"""
    for (x,y,w,h) in dogs:
        # 画bounding box（红色矩形，线宽2px）
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        
        # 添加标签（白色文字，字号0.7）
        cv2.putText(img, 'Dog', (x, y-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
    
    return img

# 主流程
if __name__ == "__main__":
    # 读取测试图像
    img = cv2.imread('./OpenCV_files/dog.jpg')
    
    # 模拟特征提取（对应图片左侧流程）
    yellow_mask, hog_feat, lbp = extract_handcrafted_features(img)
    
    # 执行检测（对应图片右侧流程）
    dogs = detect_dogs(img)
    
    # 可视化结果
    result_img = visualize_detection(img.copy(), dogs)
    
    # 显示结果
    cv2.imshow('Dog Detection', result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()