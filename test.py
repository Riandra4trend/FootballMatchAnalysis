import cv2

cap = cv2.VideoCapture("input_video/08fd33_4.mp4")
if not cap.isOpened():
    print("❌ Failed to open video.")
else:
    print("✅ Video opened successfully.")
