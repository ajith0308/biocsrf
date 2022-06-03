import cv2  
import numpy as np    
# using imread('path') and 0 denotes read as  grayscale image    
img = cv2.imread('C:/Users/ajith/Desktop/Main_Project_scf/Fin_base/static/check/f3.bmp',0)    
img_1 = cv2.boxFilter(img, 0, (7,7), img, (-1,-1), False, cv2.BORDER_DEFAULT)  
print(type(img_1))
#This is using for display the image   
cv2.imshow('Image',img_1)  
cv2.waitKey(0) # This is necessary to be required so that the image doesn't close immediately.    
#It will run continuously until the key press.    
cv2.destroyAllWindows() 
