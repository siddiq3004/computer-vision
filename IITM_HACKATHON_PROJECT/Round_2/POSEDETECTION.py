
import cv2
import mediapipe as mp
import time

mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()
rh=[]
ra=[]


cap=cv2.VideoCapture('video.mp4')
pTime=0

out = cv2.VideoWriter('output.mp4', -1, 24.0, (1280,720))

while True:
    success, img=cap.read()
    # humanImg = img.copy()
    img=cv2.resize(img,(1280,720))
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= pose.process(imgRGB)


    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c =img.shape
            if id == 24:
                rh=(id,lm)
                # print(id,lm)
                # print(rh)
                cx, cy = int(lm.x * w), int(lm.y * h)
                rightw = [cx, cy]
                # cv2.circle(img,(cx,cy),10,(255,0,0),-1)

            elif id==28:
                ra = (id, lm)
                # print(id,lm)
                # print(ra)
                cx, cy = int(lm.x * w), int(lm.y * h)
                rightl = [cx, cy]
                # cv2.circle(img, (cx, cy), 10, (255, 0, 0), -1)

            elif id==23:
                ra = (id, lm)
                # print(id,lm)
                # print(ra)
                cx, cy = int(lm.x * w), int(lm.y * h)
                leftw = [cx, cy]
                # cv2.circle(img, (cx, cy), 10, (255, 0, 0), -1)

            elif id==27:
                ra = (id, lm)
                # print(id,lm)
                # print(ra)
                cx, cy = int(lm.x * w), int(lm.y * h)
                leftl = [cx, cy]
                # cv2.circle(img, (cx, cy), 10, (255, 0, 0), -1)

            elif id==20:
                ra = (id, lm)
                # print(id,lm)
                # print(ra)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lefth = [cx, cy]
                # cv2.circle(img, (cx, cy), 10, (255, 0, 0), -1)

            elif id==19:
                ra = (id, lm)
                # print(id,lm)
                # print(ra)
                cx, cy = int(lm.x * w), int(lm.y * h)
                righth = [cx, cy]
                # cv2.circle(img, (cx, cy), 10, (255, 0, 0), -1)


    def distance(list1, list2):
        """Distance between two vectors."""
        squares = [(p - q) ** 2 for p, q in zip(list1, list2)]
        return sum(squares) ** .5


    drwl = distance(rightw, rightl)
    dlwl = distance(leftw, leftl)
    drhl = distance(righth, rightl)
    dlhl = distance(lefth, leftl)
    drhw = distance(righth, rightw)
    dlhw = distance(lefth, leftw)

    # print(drhl, dlhl)

    font = cv2.FONT_HERSHEY_SIMPLEX
    textloc = (10, 500)
    fontScale = 1
    fontColor = (255, 0, 255)
    thickness = 2
    lineType = 2
    frame_no = 0



    if drhl < 100 or dlhl < 150:
        if drwl < 200 or dlwl < 150 or drhw < 100 or dlhw < 100:
            cv2.putText(img, 'Professional Lift',
                        textloc,
                        font,
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)
        elif drhl < 100 or dlhl < 100:
            cv2.putText(img, 'Professional Lift',
                        textloc,
                        font,
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)
        else:
            cv2.putText(img, 'Unprofessional Lift',
                        textloc,
                        font,
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)


    cv2.imshow("image", img)

    cTime =time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, str(int(fps)), (70,70), font, 3, (255, 0, 0), 3)

    out.write(img)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows

# print(rh)


