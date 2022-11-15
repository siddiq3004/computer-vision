import cv2
# cap = cv2.VideoCapture(0)
# print(cap.get(3))
# print(cap.get(4))
# cap.set(3,3000)
# cap.set(4,3000)
# print(cap.get(3))
# print(cap.get(4))
# while(cap.isOpened()):
#     ret,frame = cap.read()
#     if ret == True:
#         text = 'width'+str(cap.get(3)) + 'Height'+str(cap.get(4))
#         font = cv2.FONT_HERSHEY_COMPLEX
#         frame = cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
#         cv2.imshow('frame',frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else :
#         break

# date and time
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        date_time = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_COMPLEX
        frame = cv2.putText(frame,date_time,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
