import cv2

cap = cv2.VideoCapture("D:\ciic-iitm\image processing\FullSizeRender.MOV")


frame_no = 0
while(cap.isOpened()):
    frame_exists, curr_frame = cap.read()
    if frame_exists:
        print("for frame : " + str(frame_no) + "   timestamp is: ", str(frame_no/cap.get(cv2.CAP_PROP_FPS)))
        frame_no+=1
    else:
        break
    #frame_no += 1

cap.release()