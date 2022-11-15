import numpy as np
import cv2
cap = cv2.VideoCapture('vid.mp4')

# take first frame of the video
ret , frame = cap.read()
# setup initial location of window 
x , y , width , height = 300,630,60,60
track_window = (x,y,width,height)
# set up the roi for tracking
roi = frame[y:y+height , x: x+width]

cv2.imshow('roi',roi) 
while(1):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame',frame)
        k = cv2.waitKey(27) & 0xff

        if k== 27:
            break
    else :
        break