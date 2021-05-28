# Import cv2
import cv2

# Import mediapipe as mp
import mediapipe as mp

# Import time. This is for checking frame rate
import time

# Create video object and assign it a camera
cap = cv2.VideoCapture(0)

# Create a while true statement that will give us our frame
while True:
    success, img = cap.read()

    # Create imshow and waitkey statements
    cv2.imshow("Image", img)
    cv2.waitKey(1)
