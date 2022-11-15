
import cv2
cap =cv2.VideoCapture(0); 
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#  CAP_PROP_FRAME_WIDTH------------>3 (Pre deifined property )
#  CAP_PROP_FRAME_HEIGHT------------>4 (Pre deifined property )
cap.set(3,1280)
cap.set(4,720)

print(cap.get(3))
print(cap.get(4))
while (True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()