import cv2
import torch
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 Large model
model = YOLO("yolov8l.pt")

# Check for GPU availability
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define target class
TARGET_CLASS = "bottle"
CONFIDENCE_THRESHOLD = 0.5  # Adjust as needed
IOU_THRESHOLD = 0.3

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB (YOLO expects RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run YOLO inference (stream=True for better performance)
    results = model(frame_rgb, iou=IOU_THRESHOLD, conf=CONFIDENCE_THRESHOLD, stream=True)

    # Process results
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0].item())  # Class index
            label = model.model.names[cls]  # Get class name
            
            if label == TARGET_CLASS:
                conf = box.conf[0].item()
                if conf >= CONFIDENCE_THRESHOLD:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    # Draw bounding box and label
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label} ({conf:.2f})", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # Show frame
    cv2.imshow('Frame', frame)

    # Press 'ESC' to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
