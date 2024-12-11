import cv2
from goprocam import GoProCamera

def get_live_feed():
    # Initialize the GoPro camera
    gpCam = GoProCamera.GoPro()

    # Open the video capture
    # The URL "udp://127.0.0.1:10000" suggests the stream is being received on your local machine
    cap = cv2.VideoCapture("udp://127.0.0.1:10000")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Display the resulting frame
        cv2.imshow("GoPro Live Feed", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    get_live_feed()