import cv2
import serial
import time

# --- User Parameters ---
SERIAL_PORT = 'COM8'
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

lower_green = (35, 100, 100)   # Adjust based on lighting conditions
upper_green = (85, 255, 255)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert frame to HSV (common for color detection)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for red color
    # Create masks for red and green
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    # Combine masks if necessary.

    # Check if we see something red
    # For simplicity, just check if there's a significant number of red pixels
    red_pixels = cv2.countNonZero(mask_red)
    green_pixels = cv2.countNonZero(mask_green)
    height, width = frame.shape[:2]
    # A simple threshold: if more than 5% of the frame is red, we act
    # Decision logic based on detected colors
    if red_pixels > (0.05 * height * width):
        command = "MOVE_LEFT\n"
    elif green_pixels > (0.05 * height * width):
        command = "MOVE_RIGHT\n"
    else:
        command = "STOP\n"

    # Send the command to Arduino
    ser.write(command.encode('utf-8'))
    response = ser.readline().decode('utf-8').strip()
    print(f"Arduino says: {response}")

    # Show video feed with masks
    cv2.imshow('Video', frame)
    cv2.imshow('Red Mask', mask_red)
    cv2.imshow('Green Mask', mask_green)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
ser.close()
