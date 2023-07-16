import cv2
import os

# Function to save image with label
def save_image(image, label, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    count = len(os.listdir(output_dir))
    filename = f"{label}_{count}.jpg"
    filepath = os.path.join(output_dir, filename)
    cv2.imwrite(filepath, image)
    print(f"Image saved: {filepath}")

# Constants for region of interest (ROI)
ROI_TOP = 150
ROI_BOTTOM = 350
ROI_LEFT = 100
ROI_RIGHT = 300

# Constants for capturing images
NUM_IMAGES = 20
OUTPUT_DIR = "sign_images"

# Define the labels
LABELS = ["Hello",'Yes','No','Thanks']

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a window to display the webcam feed
cv2.namedWindow("Capture")

# Initialize variables
images_captured = 0
current_label_index = 0

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Draw the region of interest (ROI) rectangle
    cv2.rectangle(frame, (ROI_LEFT, ROI_TOP), (ROI_RIGHT, ROI_BOTTOM), (0, 255, 0), 2)
    
    # Display instructions
    cv2.putText(frame, f"Capture images for: {LABELS[current_label_index]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, f"Images captured: {images_captured}/{NUM_IMAGES}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "Press spacebar to capture", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "Press 'q' to quit", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # Display the frame
    cv2.imshow("Capture", frame)
    
    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    
    # Capture image if spacebar is pressed
    if key == ord(" "):
        if images_captured < NUM_IMAGES:
            # Capture image within the region of interest
            image_roi = frame[ROI_TOP:ROI_BOTTOM, ROI_LEFT:ROI_RIGHT]
            
            # Get the current label
            current_label = LABELS[current_label_index]
            
            # Save the image with the current label
            save_image(image_roi, current_label, OUTPUT_DIR)
            
            images_captured += 1
            if images_captured == NUM_IMAGES:
                print("Image capture complete.")
                if current_label_index == len(LABELS) - 1:
                    print("All labels captured.")
                    break
                else:
                    images_captured = 0
                    current_label_index += 1
    
    # Quit if 'q' is pressed
    if key == ord("q"):
        break

# Release the webcam and close the windows
cap.release()
cv2.destroyAllWindows()
