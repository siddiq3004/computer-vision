import cv2
img = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv-logo.png')
print(img.shape) #returs tuples of rows,columns, and channels
print(img.size) # return Total number of pixels is accessed
print(img.dtype) # returns image datatype is obtained
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340,330:390]
img[273:333,100:160] = ball

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
# dst = cv2.add(img2 , img)
dst = cv2.addWeighted(img ,.5, img2, .5 , 0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()