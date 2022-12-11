import cv2

#%% detect lowerbody in video

video_path = "lowerbody_test.mp4"
window_name = f"Detected Objects in {video_path}"
video = cv2.VideoCapture(video_path)

while True:
    # read() returns a boolean alongside the image data if it was successful
    ret, frame = video.read()
    # Quit if no image can be read from the video
    if not ret:
        break
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # Greyscale image for classification
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Define classifier
    cascade_classifier = cv2.CascadeClassifier(
        f"{cv2.data.haarcascades}haarcascade_lowerbody.xml")
    # Detect objects
    detected_objects = cascade_classifier.detectMultiScale(
        image, minSize=(50, 50))
    # Draw rectangles
    if len(detected_objects) != 0:
        for (x, y, height, width) in detected_objects:
            cv2.rectangle(
                frame, (x, y), ((x + height), (y + width)), (0, 255, 0), 15)
    #Show image
    cv2.imshow(window_name, frame)
    
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()

#%% detect lowerbody in real-time

window_name = "Detected Objects in webcam"
video = cv2.VideoCapture(0)

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade_classifier = cv2.CascadeClassifier(
        f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
    detected_objects = cascade_classifier.detectMultiScale(
        image, minSize=(20, 20))

    if len(detected_objects) != 0:
        for (x, y, height, width) in detected_objects:
            cv2.rectangle(
                frame, (x, y), ((x + height), (y + width)), (0, 255, 0), 5)
    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
