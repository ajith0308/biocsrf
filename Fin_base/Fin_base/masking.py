# Python program to explain
# mask inversion on a b/w image.

# importing cv2 and numpy library
import cv2
import numpy as np

# Reading an image
img = cv2.imread('C:/Users/ajith/Desktop/Main_Project_scf/Fin_base/static/check/f3.bmp',0)

# The kernel to be used for dilation purpose
kernel = np.ones((5, 5), np.uint8)

# converting the image to HSV format
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# defining the lower and upper values of HSV,
# this will detect yellow colour
Lower_hsv = np.array([20, 70, 100])
Upper_hsv = np.array([30, 255, 255])

# creating the mask by eroding,morphing,
# dilating process
Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
Mask = cv2.erode(Mask, kernel, iterations=1)
Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
Mask = cv2.dilate(Mask, kernel, iterations=1)

# Inverting the mask by
# performing bitwise-not operation
Mask = cv2.bitwise_not(Mask)

# Displaying the image
cv2.imshow('Mask', Mask)

# waits for user to press any key
# (this is necessary to avoid Python
# kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()

