import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fftshift
def adjust_gamma(image, gamma=1.0):
    
   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

def match(sample):
       
       gamma = 0.3
       sample1= adjust_gamma(sample, gamma=gamma)
       resultimage=np.zeros((800,800))
       normalizedimage = cv2.normalize(sample1,resultimage, 4, 100, cv2.NORM_MINMAX)
       # rio=cv2.selectROI(normalizedimage)
       f=np.fft.fft2(normalizedimage)
       fshift=np.fft.fftshift(f)
       magnitude_spectrum = 10*np.log(np.abs(fshift))
       plt.subplot(121),plt.imshow(normalizedimage, cmap = 'gray')
       plt.title('Input Image'), plt.xticks([]), plt.yticks([])
       plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
       plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
       rows, cols = normalizedimage.shape
       crow,ccol = rows//2 , cols//2
       fshift[crow-30:crow+31, ccol-30:ccol+31] = 0
       f_ishift = np.fft.ifftshift(fshift)
       img_back = np.fft.ifft2(f_ishift)
       img_back = np.real(img_back)
       img_1 = cv2.blur(img_back,(3,3))
       return img_1
   
sample=cv2.imread("C:/Users/ajith/Desktop/Main_Project_scf/Fin_base/static/check/k1.bmp",0)
sample1=cv2.imread('C:/Users/ajith/Desktop/Main_Project_scf/Fin_base/static/check/k3.bmp',0)
s1=match(sample)
s2=match(sample1)
print(s1)
print(s2)
