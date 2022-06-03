import os
import cv2
from cv2 import bitwise_not
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fftshift
def adjust_gamma(image, gamma=1.0):
    
   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)


def normalizer(sample1):
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
    plt.subplot(131),plt.imshow(normalizedimage, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # HPF=plt.imshow(img_back, cmap = 'gray')
    plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    # JET=plt.imshow(img_back)
    plt.subplot(133),plt.imshow(img_back)
    plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
    plt.show()
    img_1 = cv2.blur(img_back,(3,3))
    img_1=bitwise_not(img_1)
    image8bit = img_1.astype('uint8')
    return image8bit
    # cv2.imshow('Image',img_1)  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    

sample=cv2.imread("C:/Users/ajith/Desktop/Main_Project_scf/Fin_base/static/check/k3.bmp",0)
gamma = 0.8
sample1= adjust_gamma(sample, gamma=gamma)
proc1=normalizer(sample1)
best_scoure=0
filename=None
imag=None
kp1,p2,mp,kp2=None,None,None,None
fingerprint_img=cv2.imread('C:/Users/ajith/Desktop/Main_Project_scf/Fin_base/static/check/k1.bmp',0)
fingerprint_img1= adjust_gamma(fingerprint_img,gamma=gamma)
proc2=normalizer(fingerprint_img1)
sift=cv2.SIFT_create()
keypoint_1,description_1=sift.detectAndCompute(proc1,None)
keypoint_2,description_2=sift.detectAndCompute(proc2,None)
matches=cv2.FlannBasedMatcher({'algorithm':1,'trees':10},{}).knnMatch(description_1,description_2,k=2)
match_point=[]
for p,q in matches:
    if p.distance<0.6*q.distance:
        match_point.append(p)
keypoints=0
if len(keypoint_1)<=len(keypoint_2):
    keypoints=len(keypoint_1)
else:
    keypoints=len(keypoint_2)

if len(match_point) / keypoints*100 >best_scoure:
        best_scoure=len(match_point) / keypoints*100
        image=proc2
        kp1,kp2,mp=keypoint_1,keypoint_2,match_point
print('Scoure ' + str(best_scoure))
result=cv2.drawMatches(proc1,kp1,proc2,kp2,mp,None)
#result=cv2.resize(result,fx=1.5,fy=1.5)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()


