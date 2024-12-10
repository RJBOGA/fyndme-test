import cv2
import torch
import numpy as np
import os

# Loading the YOLOv5 Model
def load_model():
    # Using YOLOv5 small model (yolov5s)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

# Preprocessing the Image
def preprocess_image(image_path):
    image = cv2.imread(image_path)  # Read image
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    return image

# Performing Inference
def detect_objects(model, image):
    results = model(image)  # Run detection
    return results

# Visualizeing the Results
def visualize_results(image, results):
    df = results.pandas().xyxy[0]  # Extracting detection results as a pandas DataFrame
    for _, row in df.iterrows():
        x1, y1, x2, y2, confidence, cls, name = row[
            ["xmin", "ymin", "xmax", "ymax", "confidence", "class", "name"]
        ]
        # Draw bounding box/outline
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        # Labelling
        label = f"{name} ({confidence:.2f})"
        cv2.putText(image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

# Main
def main():
    model = load_model()  # Loading YOLOv5 model
    image_path = "sample_images/laptop.jpg"  #input image path
    image = preprocess_image(image_path)  # Loading and preprocess the image
    results = detect_objects(model, image)  # detecting the object
    output_image = visualize_results(image, results)  # Draw bounding boxes on the image
    
    # Output/ Save and display results
    output_path = "output.jpg"
    cv2.imwrite(output_path, output_image)
    print(f"Output saved to {output_path}")
    cv2.imshow("Detection Results", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
