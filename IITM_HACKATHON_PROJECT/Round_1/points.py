import cv2
import time

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height =int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)





xc=[]
yc=[]
coord={}
def mousepoints(event,x,y,flags,params):
    font=cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        xc.append(x)
        yc.append(y)
        cv2.putText(frame_resize,'.',(x,y),font,1,(255,0,0),2)
        cv2.imwrite('new.cap',frame_resize)
        cv2.imshow('cappppp',frame_resize)

cap = cv2.VideoCapture("Hackathon video.mov")
while True:
    sucess,new = cap.read()

    frame_resize=rescaleFrame(new,scale=0.55)

   # cv2.imshow("test2",new)
    cv2.imshow('video res',frame_resize)

    # newcap=cv2.VideoCapture(frame_resize)
    cv2.imshow("newcapppp",new)
    cv2.setMouseCallback("new capp", mousepoints)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()