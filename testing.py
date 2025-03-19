from PIL import Image
from ultralytics import YOLO
# Perform inference on a test image
model =YOLO('/Users/adityapnv/Desktop/Documents/YOLO-BCCD/runs/detect/train/weights/best.pt')
results = model("/Users/adityapnv/Desktop/Documents/YOLO-BCCD/example.jpg")

# Display results
for r in results:
    im_array = r.plot()  # Plot predictions
    im = Image.fromarray(im_array[..., ::-1])  # Convert to RGB
    im.show()