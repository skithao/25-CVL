#!/bin/bash
echo "即将下载COCO数据集，请稍等..."
echo "正在安装parallel工具...
sudo apt install parallel
echo "正在下载COCO数据集..."
parallel -j 4 wget -nv {} ::: http://images.cocodataset.org/zips/train2017.zip http://images.cocodataset.org/zips/val2017.zip http://images.cocodataset.org/zips/test2017.zip http://images.cocodataset.org/annotations/annotations_trainval2017.zip
