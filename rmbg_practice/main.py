import cv2
import numpy as np
from rembg import remove
img1_path = '1.jpg'
img2_path = '2.jpg'
output1_path = 'rembg1.png'
output2_path = 'rembg2.png'
roi1_path = 'r0i1.jpg'
roi2_path = 'roi2.jpg'
img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

img1_copy = img1.copy()
img2_copy = img2.copy()

img1 = cv2.resize(img1,(700,500))
img2 = cv2.resize(img2,(700,500))

# select ROI for two images -----1.jpg,2.jpg

roi1 = cv2.selectROI(img1)
roi2= cv2.selectROI(img2)

print('roi1:',roi1)
print('roi2:',roi2)

img1_cropped = img1[int(roi1[1]):int(roi1[1]+roi1[3]),
                int(roi1[0]):int(roi1[0]+roi1[2])]
img2_cropped = img2[int(roi2[1]):int(roi2[1]+roi2[3]),
                int(roi2[0]):int(roi2[0]+roi2[2])]
img1_cropped = cv2.resize(img1_cropped,(200,300))
img2_cropped = cv2.resize(img2_cropped,(700,500))
output1 = remove(img1_cropped)
output2 = remove(img2_cropped)

cv2.imwrite(output1_path, output1)
cv2.imwrite(output2_path, output2)
cv2.imwrite(roi1_path, img1_cropped)
cv2.imwrite(roi2_path, img2_cropped)
cv2.imshow('ROI1',img1_cropped)
cv2.imshow('ROI2',img2_cropped)
cv2.imshow('rembg_1',output1)
cv2.imshow('rembg_2',output2)

# drawing edges on the original image using template matching

grey_img1 = cv2.cvtColor(img1_copy,cv2.COLOR_BGR2GRAY)
grey_img2 = cv2.cvtColor(img2_copy,cv2.COLOR_BGR2GRAY)
template1 = cv2.imread('crop_1.jpg',0)
template2 = cv2.imread('crop_2.jpg',0)
w1,h1 = template1.shape[::-1 ]
w2,h2 = template2.shape[::-1 ]

res1 = cv2.matchTemplate(grey_img1,template1,cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(grey_img2,template2,cv2.TM_CCOEFF_NORMED)

threshold = 0.9
loc1 = np.where(res1 >= threshold)
loc2 = np.where(res2 >= threshold)
print(loc1)
for pt in zip(*loc1[::-1]):
    cv2.rectangle(img1_copy,pt, (pt[0]+w1, pt[1]+h1),(0,0,255),2)
for pt in zip(*loc2[::-1]):
    cv2.rectangle(img2_copy,pt, (pt[0]+w2, pt[1]+h2),(0,0,255),2)
img1_copy = cv2.resize(img1_copy,(700,500))
img2_copy = cv2.resize(img2_copy,(700,500))
cv2.imshow('output_1',img1_copy)
cv2.imshow('output_2',img2_copy)
# cv2.imshow('img2',img2_copy)
cv2.waitKey(0) 
cv2.destroyAllWindows()










# methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
# for method in methods:
#     res1 = cv2.matchTemplate(grey_img1,template1,method)
    # res2 = cv2.matchTemplate(grey_img2,template2,cv2.TM_CCOEFF_NORMED)
    # threshold = 0.9
    # res1 = np.where(res1 >= threshold)
    # print(res1)
    # min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res1)
    # if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
    #     location = min_loc
    # else:
    #     location = max_loc
    # bottom_right = (location[0]+w1 , location[1]+h1)
    # cv2.rectangle(img1_copy,location, bottom_right,(0,0,255),2)

# print(res1)
# print('rs1[0][1]:',res1[0][0])
# for res in res1:
#     for pts in res:
        # cv2.polylines(img1_copy,[pts],True, (0,255,255),2)
        # cv2.drawContours(img1_copy,[pts], -1, (0,255,0), 3)
# min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res1)
# print('min-loc:',min_loc)
# print('max-loc:',max_loc)