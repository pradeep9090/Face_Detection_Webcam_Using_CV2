import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw a rectangle around the faces and add text annotation
    for (x, y, w, h) in faces:
        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Calculate the position for the text (bottom-right of the rectangle)
        text_position = (x + w - 30, y + h + 30)
        # Ensure text does not go outside the frame
        if text_position[1] + 30 > frame.shape[0]:
            text_position = (text_position[0], frame.shape[0] - 10)
        if text_position[0] + 100 > frame.shape[1]:
            text_position = (frame.shape[1] - 100, text_position[1])
        
        # Add text below the rectangle
        cv2.putText(frame, 'Face', text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Face Detection", frame)
    
    # Break the loop if 's' key is pressed
    if cv2.waitKey(1) == ord("s"):
        break

cap.release()
cv2.destroyAllWindows()
