# BCCD-using-YOLOV8
This project is an end-to-end implementation of an object detection web app designed to detect and classify blood cells (RBC, WBC, and Platelets) using a fine-tuned YOLO-based model. The app allows users to upload an image, performs inference using the trained model.

The goal of this project is to create an interactive web app that uses a fine-tuned object detection model to identify and classify blood cells in images. The app is built using Streamlit or Gradio and deployed on Hugging Face Spaces for accessibility. The model is trained on the BCCD Dataset , which contains annotated images of blood cells.
Features
Object Detection : Detects RBCs, WBCs, and Platelets in uploaded images.
Bounding Boxes : Displays bounding boxes around detected objects with class labels and confidence scores.
Metrics Table : Shows precision and recall for each class (RBC, WBC, Platelets) and overall performance.
Interactive Interface : Built using Streamlit or Gradio for a user-friendly experience.
Deployment : Hosted on Hugging Face Spaces for easy access.

Ensure the fine-tuned model (best.onnx or equivalent) is placed in the model/ directory.
