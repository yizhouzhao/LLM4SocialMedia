
import pyautogui
import numpy as np
import cv2

# Define the coordinates of the top-left and bottom-right vertices


# Capture a screenshot of the specified region
image = pyautogui.screenshot()

# Convert the screenshot to a format compatible with OpenCV (BGR)
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

height, width, _ = image.shape

# Calculate the midpoint to split the image into left and right halves
midpoint = width // 2

# Crop the left half of the image
left_half = image[:, :midpoint]

# Save the left half as a new PNG file
cv2.imwrite("left_half.png", left_half)


