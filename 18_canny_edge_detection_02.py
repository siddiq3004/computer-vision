import cv2
import numpy as np
# from matplotlib import pyplot as plt
def nothing(x):
    pass
cv2.namedWindow('canny')
img = cv2.imread('lena.jpg',0)
cv2.createTrackbar('th1','canny',0,255,nothing)
cv2.createTrackbar('th2','canny',0,255,nothing)

while(1):
    # cv2.imshow('image',img)
    
    th1 = cv2.getTrackbarPos('th1','canny')
    th2 = cv2.getTrackbarPos('th2','canny')

    canny = cv2.Canny(img,th1,th2)

    cv2.imshow('original',img)
    cv2.imshow('canny',canny)
    k = cv2.waitKey(1) & 0xFF
    if k== 27 :
        break
cv2.destroyAllWindows()
# titles =['image','canny']
# images =[img,canny]
# for i in range(2):
#     plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()