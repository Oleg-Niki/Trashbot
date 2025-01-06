import cv2
import serial
import time

# --- User Parameters ---
SERIAL_PORT = 'COM7'
BAUD_RATE = 9600
CAMERA_INDEX = 0       # 0 for default webcam

# Initialize serial connection to Arduino
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Give the Arduino time to reset if needed

ser.write(b"MOVE_LEFT\n")
response = ser.readline().decode('utf-8', 'ignore').strip()
print("Arduino says:", response)

# Open the webcam
cap = cv2.VideoCapture(CAMERA_INDEX)
if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

# Example: We want to recognize a certain color (e.g., red object) and send a command.

# Define color range in HSV for the object we want to detect (e.g., a red object)
# Adjust these values depending on your object and lighting conditions.
lower_red = (170, 120, 70)
upper_red = (179, 255, 255)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert frame to HSV (common for color detection)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for red color
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # Optional: Add a second range for red if needed (e.g., upper hue range)
    # Combine masks if necessary.

    # Check if we see something red
    # For simplicity, just check if there's a significant number of red pixels
    red_pixels = cv2.countNonZero(mask)
    height, width = frame.shape[:2]
    # A simple threshold: if more than 5% of the frame is red, we act
    if red_pixels > (0.05 * height * width):
        # Send a command to Arduino if red object is detected
        command = "MOVE_LEFT\n"
        ser.write(command.encode('utf-8'))
        # Read response
        response = ser.readline().decode('utf-8').strip()
        print("Arduino says:", response)
    else:
        # Otherwise, send a stop command
        command = "STOP\n"
        ser.write(command.encode('utf-8'))
        # Read response
        response = ser.readline().decode('utf-8').strip()
        print("Arduino says:", response)

    # Show the video feed
    cv2.imshow('Video', frame)
    cv2.imshow('Mask', mask)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
ser.close()
