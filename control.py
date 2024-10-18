import serial
import cv2
import time

# Set up serial communication with Arduino
arduino_port = 'COM6'  # Change this to your Arduino port
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Set up video capture
cap = cv2.VideoCapture(0)  # Use 0 for default camera

# Define video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

def send_command_and_record():
    user = input("Want to send rotate command? Type 'y' for yes and 'n' for no: ")

    if user.lower() == 'y':
        ser.write(b'rotate\n')
        print("Command sent")
        
        recording = True
        while recording:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                cv2.imshow('Recording', frame)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            # Check for the 'complete' message from Arduino
            if ser.in_waiting > 0:
                message = ser.readline().decode('utf-8').strip()
                if message == 'complete':
                    print("Rotation complete, stopping recording")
                    recording = False

        # Release everything
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    else:
        ser.write(b'no\n')
        print("Command not sent")
        

            

# Main execution
if __name__ == "__main__":
    try:
        while True:
            send_command_and_record()
    finally:
        ser.close()  # Ensure serial connection is closed

print("Video saved as output.avi")