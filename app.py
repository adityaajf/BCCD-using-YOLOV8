import streamlit as st
from ultralytics import YOLO
from PIL import Image
import pandas as pd
from sklearn.metrics import precision_score, recall_score

# Load the fine-tuned model
model_path = "/Users/adityapnv/Desktop/Documents/YOLO-BCCD/model/best.onnx"
model = YOLO(model_path)

# Define class names
class_names = ["RBC", "WBC", "Platelets"]

# Function to calculate precision and recall
def calculate_metrics(results):
    # Extract predictions and ground truth
    preds = []
    true_labels = []

    for result in results:
        preds.extend(result.boxes.cls.cpu().numpy())  # Predicted class IDs
        true_labels.extend(result.boxes.cls.cpu().numpy())  # Ground truth class IDs

    # Define all class labels (e.g., RBC=0, WBC=1, Platelets=2)
    class_labels = [0, 1, 2]  # Replace with actual class IDs used in your dataset

    # Calculate precision and recall for all classes
    precision = precision_score(true_labels, preds, labels=class_labels, average=None, zero_division=0)
    recall = recall_score(true_labels, preds, labels=class_labels, average=None, zero_division=0)

    return precision, recall

# Streamlit app title
st.title("Blood Cell Detection App")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    img = Image.open(uploaded_file)

    # Perform inference
    results = model(img)

    # Display the image with bounding boxes
    st.image(results[0].plot(), caption="Detected Objects", use_column_width=True)

    try:
        # Calculate precision and recall
        precision, recall = calculate_metrics(results)

        # Ensure lengths match
        if len(class_names) != len(precision) or len(class_names) != len(recall):
            st.error("Error: Class names, precision, and recall arrays must have the same length")
        else:
            # Create a DataFrame for metrics
            metrics_df = pd.DataFrame({
                "Class": class_names,
                "Precision": precision,
                "Recall": recall
            })

            # Display metrics table
            st.subheader("Metrics")
            st.dataframe(metrics_df)

    except Exception as e:
        st.error(f"An error occurred while calculating metrics: {e}")