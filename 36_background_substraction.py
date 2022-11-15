import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
# kernal = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
# fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
# fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False)
fgbg = cv.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    fgmask = fgbg.apply(frame)
    # fgmask = cv.morphologyEx(fgmask,cv.MORPH_OPEN,kernal)
    cv.imshow('frame',frame)
    cv.imshow('FG MASK FRAME',fgmask)
    keyboard = cv.waitKey(30)
    if keyboard =='q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()