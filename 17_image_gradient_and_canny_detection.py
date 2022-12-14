import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png',0)
img1 = cv2.imread('messi.jpg',0)
lap = cv2.Laplacian(img , cv2.CV_64F,ksize=1)
lap = np.uint8(np.absolute(lap))
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelcombined = cv2.bitwise_or(sobelx,sobely)
canny = cv2.Canny(img1,100,200)
titles = ['image','Laplacian','sobelx','sobely','sobelcombined','canny']
images = [img,lap,sobelx,sobely,sobelcombined,canny]
for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
