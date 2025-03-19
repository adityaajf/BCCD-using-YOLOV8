from ultralytics import YOLO
model =YOLO('/Users/adityapnv/Desktop/Documents/YOLO-BCCD/runs/detect/train/weights/best.pt')
metrics = model.val()
print(metrics)