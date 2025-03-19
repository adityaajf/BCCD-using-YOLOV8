from ultralytics import YOLO
model =YOLO('/Users/adityapnv/Desktop/Documents/YOLO-BCCD/runs/detect/train/weights/best.pt')
model.export(format="onnx")