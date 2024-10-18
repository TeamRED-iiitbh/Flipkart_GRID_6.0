import cv2
import numpy as np
from goprocam import GoProCamera

def get_live_feed():
    


    # Open the video capture
    cap = cv2.VideoCapture('http://192.168.184.135:8080/video')

    while True:
        # Read a frame from the stream
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the frame
        cv2.imshow("GoPro Live Feed", frame)
        print(frame.shape)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()

    

if __name__ == "__main__":
    get_live_feed()