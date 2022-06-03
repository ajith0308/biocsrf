import cv2
import numpy as np
#reading the image to be normalized using imread() function
imageread = cv2.imread('C:/Users/ajith/Desktop/Main_Project_scf/Fin_base/static/check/f3.bmp',0)
#setting the array for resulting image after normalization
resultimage = np.zeros((800, 800))
#normalizing the given image using normalize() function
normalizedimage = cv2.normalize(imageread,resultimage, 0, 100, cv2.NORM_MINMAX)
#displaying the normalized image as the output on the screen
cv2.imshow('Normalized_image', normalizedimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
