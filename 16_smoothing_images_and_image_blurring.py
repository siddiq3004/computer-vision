import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('apple.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernal)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateralFilter = cv2.bilateralFilter(img,9,75,75)
titles = ['image','2D convolution','blur','GuassianBlur' , 'bilateralFilter']
images = [img , dst , blur , gblur , bilateralFilter]

for i in range(5):
    plt.subplot(3,2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()