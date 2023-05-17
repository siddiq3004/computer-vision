import os
import contrib
import cv2
import datetime
import numpy as np
import mediapipe as mp
from glob import glob
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('Hackathon video.mov')
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
dimensions = []


# -------------------- extracting frames ----------------------------------
def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR : creating directory with name {path}")


def save_frame(video_path, save_dir):
    name = video_path.split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0
    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break

        cv2.imwrite(f"{save_path}/{idx}.png", frame)
        idx += 1


if __name__ == "__main__":
    video_paths = glob('video.mov')
    save_dir = 'save'
    for path in video_paths:
        save_frame(path, save_dir)

# ------------------------------***********-----------------------------

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1200, 700))
    # -----------------------------creating ROI (region of intrest)-------------------------------
    # drawing first quadrant
    p1 = (19, 288)
    p2 = (334, 135)
    p3 = (611, 231)

    cv2.line(frame, p1, p2, (255, 0, 0), 3)
    cv2.line(frame, p2, p3, (255, 0, 0), 3)
    cv2.line(frame, p1, p3, (255, 0, 0), 3)
    centroid = ((p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3)
    cv2.circle(frame, centroid, 4, (0, 255, 0))

    p1 = (19, 288)
    p4 = (306, 431)
    p3 = (611, 231)

    cv2.line(frame, p1, p4, (255, 0, 0), 3)
    cv2.line(frame, p4, p3, (255, 0, 0), 3)
    cv2.line(frame, p1, p3, (255, 0, 0), 3)
    centroid = ((p1[0] + p4[0] + p3[0]) // 3, (p1[1] + p4[1] + p3[1]) // 3)
    cv2.circle(frame, centroid, 4, (0, 255, 0))

    # drawing second quadrant
    p21 = (334, 135)
    p22 = (562, 20)
    p23 = (825, 90)

    cv2.line(frame, p21, p22, (0, 0, 255), 3)
    cv2.line(frame, p22, p23, (0, 0, 255), 3)
    cv2.line(frame, p21, p23, (0, 0, 255), 3)
    centroid = ((p21[0] + p22[0] + p23[0]) // 3, (p21[1] + p22[1] + p23[1]) // 3)
    cv2.circle(frame, centroid, 4, (0, 255, 0))

    p21 = (334, 135)
    p24 = (611, 231)
    p23 = (825, 90)

    cv2.line(frame, p21, p24, (0, 0, 255), 3)
    cv2.line(frame, p24, p23, (0, 0, 255), 3)
    cv2.line(frame, p21, p23, (0, 0, 255), 3)
    centroid = ((p21[0] + p24[0] + p23[0]) // 3, (p21[1] + p24[1] + p23[1]) // 3)
    cv2.circle(frame, centroid, 4, (0, 255, 0))

    # drawing third quadrant
    p31 = (306, 431)
    p32 = (611, 231)
    p33 = (985, 362)

    cv2.line(frame, p31, p32, (0, 255, 0), 3)
    cv2.line(frame, p32, p33, (0, 255, 0), 3)
    cv2.line(frame, p31, p33, (0, 255, 0), 3)
    centroid = ((p31[0] + p32[0] + p33[0]) // 3, (p31[1] + p32[1] + p33[1]) // 3)
    cv2.circle(frame, centroid, 4, (0, 255, 0))

    p31 = (306, 431)
    p34 = (708, 640)
    p33 = (985, 362)

    cv2.line(frame, p31, p34, (0, 255, 0), 3)
    cv2.line(frame, p34, p33, (0, 255, 0), 3)
    cv2.line(frame, p31, p33, (0, 255, 0), 3)
    centroid = ((p31[0] + p34[0] + p33[0]) // 3, (p31[1] + p34[1] + p33[1]) // 3)
    cv2.circle(frame, centroid, 4, (0, 255, 0))

    # drawing fourth quadrant
    p41 = (611, 231)
    p42 = (825, 90)
    p43 = (1171, 178)

    cv2.line(frame, p41, p42, (0, 0, 0), 3)
    cv2.line(frame, p42, p43, (0, 0, 0), 3)
    cv2.line(frame, p41, p43, (0, 0, 0), 3)
    centroid = ((p41[0] + p42[0] + p43[0]) // 3, (p41[1] + p42[1] + p43[1]) // 3)
    cv2.circle(frame, centroid, 4, (0, 255, 0))

    p41 = (611, 231)
    p44 = (985, 362)
    p43 = (1171, 178)

    cv2.line(frame, p41, p44, (0, 0, 0), 3)
    cv2.line(frame, p44, p43, (0, 0, 0), 3)
    cv2.line(frame, p41, p43, (0, 0, 0), 3)
    centroid = ((p41[0] + p44[0] + p43[0]) // 3, (p41[1] + p44[1] + p43[1]) // 3)
    cv2.circle(frame, centroid, 4, (0, 255, 0))

    # total Roi
    pt1 = (19, 288)
    pt2 = (562, 20)
    pt3 = (1171, 178)

    cv2.line(frame, pt1, pt2, (200, 200, 255), 3)
    cv2.line(frame, pt2, pt3, (200, 200, 255), 3)
    cv2.line(frame, pt1, pt3, (200, 200, 255), 3)

    pt1 = (19, 288)
    pt4 = (708, 640)
    pt3 = (1171, 178)

    cv2.line(frame, pt1, pt4, (200, 200, 255), 3)
    cv2.line(frame, pt4, pt3, (200, 200, 255), 3)
    cv2.line(frame, pt1, pt3, (200, 200, 255), 3)
    # -------------------------creating ball detection or object detection----------------------------
    kernal = np.ones((2, 2), np.uint8)
    mask = object_detector.apply(frame)
    mask = cv2.resize(mask, (1200, 700))
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
    res = cv2.bitwise_and(frame, frame, mask=opening)
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    i = 0
    # ----------------drawing contours for ball detection---------------------
    if len(contours) != 0:
        cnt = contours[0]
        M = cv2.moments(cnt)
        Cx = int(M['m10'] / M['m00'])
        Cy = int(M['m01'] / M['m00'])
        S = 'Location of object:' + '(' + str(Cx) + ',' + str(Cy) + ')'
        cv2.putText(frame, S, (5, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.drawContours(frame, cnt, -1, (0, 255, 0), 3)
        # ----------Cx = x position of ball and Cy = y position of ball ---------------
        # dimensions.append([Cx, Cy])
        # print(Cx, Cy)

    elif len(contours) == 0:
        i += 1
        # ---------- when ball is not present in frame , then it appends 0--------------
        # dimensions.append('0')

    if ret == True:
        cv2.imshow('Original Image', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    else:
        break
# ----------- calculating the frame per second (FPS) -------------------------
fps = cap.get(cv2.CAP_PROP_FPS)  # To get fps of video
# ----------------Frames at which ball is bounced----------------------------
frames = [42, 90, 170, 219, 318, 381, 430, 529, 717, 883, 1013, 1085, 1214]
j = 0
# -----extracted quadrants by matching with bouncing points-------
extracted_quadrants = {1: 4,
                       2: 'Out of Bound',
                       3: 1,
                       4: 'Out of Bound',
                       5: 1,
                       6: 2,
                       7: 'Out of Bound',
                       8: 2,
                       9: 3,
                       10: 3,
                       11: 'Out of Bound',
                       12: 2,
                       13: 2}

# ------------Bouncing points which we extract ----------------------

Bouncing_points = [[959, 158], [1171, 13], [334, 235], [11, 26], [166, 224], [702, 88], [1082, 1],
                   [624, 112], [627, 434], [661, 280], [0, 665], [937, 481], [536, 94]]

for i in range(len(Bouncing_points)):
    if (19 < Bouncing_points[i][0] < 611):
        if (135 < Bouncing_points[i][1] < 432):
            print('Quadrant 1')

    if (334 < Bouncing_points[i][0] < 825):
        if (20 < Bouncing_points[i][1] < 231):
            print('Quadrant 2')

    if (306 < Bouncing_points[i][0] < 985):
        if (231 < Bouncing_points[i][1] < 640):
            print('Quadrant 3')

    if (611 < Bouncing_points[i][0] < 1171):
        if (178 < Bouncing_points[i][1] < 231):
            print('Quadrant 4')

    else:
        print('Out of Bound')

# ------------Calculating Time of bounce--------------
for i in range(len(frames)):
    j = j + 1
    frame = frames[i]
    seconds = frame / fps  # getting seconds of video
    video_time = datetime.timedelta(seconds=seconds)
    print("BOUNCE_NUMBER: {0:>5}\tTIME OF BOUNCE: {1:>5}\tQuadrant of Bounce: {2:>5}\t         FRAME:{3:>5}".format(j,
                                                                                                                    seconds,
                                                                                                                    extracted_quadrants[
                                                                                                                        j],
                                                                                                                    frame))

cap.release()
cv2.destroyAllWindows()