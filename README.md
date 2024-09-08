# Face Detection with OpenCV

### Prerequisites
- Python 3.12.6 or above
- OpenCV (`pip install opencv-python`)

### Features
- Detects faces in real-time using the webcam.
- Draws a rectangle around each detected face.
- Displays the label "Face" below the rectangle for better identification.
- Optimized to prevent text from going out of frame.

### Code Workflow
1. Load the pre-trained Haar Cascade face detection model.
2. Capture video frames from the webcam.
3. Convert frames to grayscale for more efficient face detection.
4. Detect faces in each frame using the `detectMultiScale` function.
5. Draw a rectangle and annotate faces with a label.
6. Display the processed video in real-time.
7. Press 's' to stop the detection and close the window.

### How to Run
1. Clone the repository and navigate to the folder.
2. Ensure your webcam is connected.
3. Run the script: `python face_detection.py`.
4. The video will open, and faces will be detected and labeled.
5. Press 's' to stop the webcam feed and close the application.

### Customization
- You can adjust the face detection sensitivity by modifying the `scaleFactor` and `minNeighbors` parameters in the `detectMultiScale` function.
