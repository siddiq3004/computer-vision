import cv2
# from orange_detector import OrangeDetector
# from kalmanfilter import KalmanFilter
#
#
#
# # Load detector
# od = OrangeDetector()
#
# # # Load Kalman filter to predict the trajectory
# # kf = KalmanFilter()

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height =int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)


cap = cv2.VideoCapture("Hackathon video.mov")
while True:
    sucess,new = cap.read()

    frame_resize=rescaleFrame(new,scale=0.55)

   # cv2.imshow("test2",new)
    cv2.imshow('video res',frame_resize)


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()