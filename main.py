import tensorflow
import cv2
import time
import os
import uuid

IMAGES_PATH = r"Tensorflow\workspace\images\collectedimages"

labels = ['a', 'b', 'c', 'd', 'e']
num_images = 15  

for label in labels:
    # Create directory for each label
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)
    
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam opened correctly
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        break

    print(f'Collecting images for {label}')
    time.sleep(5)  # Wait for 5 seconds before starting the collection
    
    for imgnum in range(num_images):
        ret, frame = cap.read()  # Capture frame from webcam
        
        if not ret:
            print("Error: Failed to capture image.")
            break
        
        # Create a unique image name using UUID
        imagename = os.path.join(IMAGES_PATH, label, f'{label}.{uuid.uuid1()}.jpg')
        
        # Save the captured image
        cv2.imwrite(imagename, frame)
        
        # Show the captured frame
        cv2.imshow('frame', frame)
        
        time.sleep(2)  # Wait for 2 seconds before capturing next image
        
        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
