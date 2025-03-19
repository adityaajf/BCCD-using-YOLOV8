from ultralytics import YOLO

# Load pre-trained YOLOv10 model
model = YOLO("yolov10n.pt")

# Fine-tune on BCCD Dataset
results = model.train(data="/Users/adityapnv/Desktop/Documents/YOLO-BCCD/bccd.yaml", epochs=3, imgsz=640, batch=16)