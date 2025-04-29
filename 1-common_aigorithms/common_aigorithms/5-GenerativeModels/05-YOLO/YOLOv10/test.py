from ultralytics import YOLOv10


model = YOLOv10('.\weights\yolov10n.pt')
model.val(data='coco.yaml', batch=256)