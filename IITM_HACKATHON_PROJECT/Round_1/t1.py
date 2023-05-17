import os
import contrib
import cv2
import numpy as np
import mediapipe as mp
from glob import glob
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('Hackathon video.mov')
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)


# extracting frames
# def create_dir(path):
#     try:
#         if not os.path.exists(path):
#             os.makedirs(path)
#     except OSError:
#         print(f"ERROR : creating directory with name {path}")

# def save_frame(video_path,save_dir):
#     name = video_path.split(".")[0]
#     save_path = os.path.join(save_dir,name)
#     create_dir(save_path)

#     cap = cv2.VideoCapture(video_path)
#     idx = 0
#     while True:
#         ret, frame = cap.read()

#         if ret == False:
#             cap.release()
#             break

#         cv2.imwrite(f"{save_path}/{idx}.png", frame)
#         idx+=1


# if _name_ == "_main_":
#     video_paths = glob('video.mov')
#     save_dir = 'save'
#     for path in video_paths:
#         save_frame(path,save_dir)


def bouncing(list1, list2):
    x_new = list1[1]
    y_new = list2[1]
    new_list1 = []
    new_list2 = []
    new_list11 = []
    new_list21 = []
    final_list_x1 = []
    final_list_y1 = []
    final_list_x2 = []
    final_list_y2 = []

    for i in range(len(list1)):
        if (list1[i + 1] >= x_new and list2[i + 1] <= y_new):
            if (list1[i + 1] != list1[i] or list2[i + 1] != list2[i]):
                new_list1.append(list1[i + 1])
                new_list2.append(list2[i + 1])
            final_list_x1.append(new_list1[-1])
            final_list_y1.append(new_list2[-1])
            print(final_list_x1)
            print(final_list_y1)
        elif (list1[i + 1] <= x_new and list2[i + 1] <= y_new):
            if (list1[i + 1] != list1[i] or list2[i + 1] != list2[i]):
                new_list11.append(list1[i + 1])
                new_list21.append(list2[i + 1])
            final_list_x2.append(new_list1[-1])
            final_list_y2.append(new_list2[-1])
            print(final_list_x2)
            print(final_list_y2)
        else:
            break


list1 = []
list2 = []

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1200, 700))

    # drawing first quadrant
    p1 = (19, 288)
    p2 = (334, 135)
    p3 = (611, 231)
    p4 = (306, 431)

    cv2.line(frame, p1, p2, (255, 0, 0), 3)
    cv2.line(frame, p2, p3, (255, 0, 0), 3)
    cv2.line(frame, p3, p4, (255, 0, 0), 3)
    cv2.line(frame, p4, p1, (255, 0, 0), 3)
    # centroid = ((p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))

    # p1 = (19, 288)
    # p4 = (306, 431)
    # p3 = (611, 231)
    #
    # cv2.line(frame, p1, p4, (255, 0, 0), 3)
    # cv2.line(frame, p4, p3, (255, 0, 0), 3)
    # cv2.line(frame, p1, p3, (255, 0, 0), 3)
    # centroid = ((p1[0] + p4[0] + p3[0]) // 3, (p1[1] + p4[1] + p3[1]) // 3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))

    # drawing second quadrant
    p21 = (334, 135)
    p22 = (562, 20)
    p23 = (825, 90)
    p24 = (611, 231)

    cv2.line(frame, p21, p22, (0, 0, 255), 3)
    cv2.line(frame, p22, p23, (0, 0, 255), 3)
    cv2.line(frame, p23, p24, (0, 0, 255), 3)
    cv2.line(frame, p24, p21, (0, 0, 255), 3)
    # centroid = ((p21[0] + p22[0] + p23[0]) // 3, (p21[1] + p22[1] + p23[1]) // 3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))

    # p21 = (334, 135)
    # p24 = (611, 231)
    # p23 = (825, 90)
    #
    # cv2.line(frame, p21, p24, (0, 0, 255), 3)
    # cv2.line(frame, p24, p23, (0, 0, 255), 3)
    # cv2.line(frame, p21, p23, (0, 0, 255), 3)
    # centroid = ((p21[0] + p24[0] + p23[0]) // 3, (p21[1] + p24[1] + p23[1]) // 3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))

    # drawing third quadrant
    p31 = (306, 431)
    p32 = (611, 231)
    p33 = (985, 362)
    p34 = (708, 640)

    cv2.line(frame, p31, p32, (0, 255, 0), 3)
    cv2.line(frame, p32, p33, (0, 255, 0), 3)
    cv2.line(frame, p33, p34, (0, 255, 0), 3)
    cv2.line(frame, p34, p31, (0, 255, 0), 3)
    # centroid = ((p31[0] + p32[0] + p33[0]) // 3, (p31[1] + p32[1] + p33[1]) // 3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))

    # p31 = (306, 431)
    # p34 = (708, 640)
    # p33 = (985, 362)
    #
    # cv2.line(frame, p31, p34, (0, 255, 0), 3)
    # cv2.line(frame, p34, p33, (0, 255, 0), 3)
    # cv2.line(frame, p31, p33, (0, 255, 0), 3)
    # centroid = ((p31[0] + p34[0] + p33[0]) // 3, (p31[1] + p34[1] + p33[1]) // 3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))

    # drawing fourth quadrant
    p41 = (611, 231)
    p42 = (825, 90)
    p43 = (1171, 178)
    p44 = (985, 362)

    cv2.line(frame, p41, p42, (0, 0, 0), 3)
    cv2.line(frame, p42, p43, (0, 0, 0), 3)
    cv2.line(frame, p43, p44, (0, 0, 0), 3)
    cv2.line(frame, p44, p41, (0, 0, 0), 3)
    # centroid = ((p41[0] + p42[0] + p43[0]) // 3, (p41[1] + p42[1] + p43[1]) // 3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))

    # p41 = (611, 231)
    # p44 = (985, 362)
    # p43 = (1171, 178)
    #
    # cv2.line(frame, p41, p44, (0, 0, 0), 3)
    # cv2.line(frame, p44, p43, (0, 0, 0), 3)
    # cv2.line(frame, p41, p43, (0, 0, 0), 3)
    # centroid = ((p41[0] + p44[0] + p43[0]) // 3, (p41[1] + p44[1] + p43[1]) // 3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))

    # total Roi
    pt1 = (19, 288)
    pt2 = (562, 20)
    pt3 = (1171, 178)
    pt4 = (708, 640)

    cv2.line(frame, pt1, pt2, (200, 200, 255), 3)
    cv2.line(frame, pt2, pt3, (200, 200, 255), 3)
    cv2.line(frame, pt3, pt4, (200, 200, 255), 3)
    cv2.line(frame, pt4, pt1, (200, 200, 255), 3)
    # # centroid = ((pt1[0]+pt2[0]+pt3[0])//3, (pt1[1]+pt2[1]+pt3[1])//3)
    #
    # pt1 = (19, 288)
    # pt4 = (708, 640)
    # pt3 = (1171, 178)
    #
    # cv2.line(frame, pt1, pt4, (200, 200, 255), 3)
    # cv2.line(frame, pt4, pt3, (200, 200, 255), 3)
    # cv2.line(frame, pt1, pt3, (200, 200, 255), 3)
    # centroid = ((pt1[0]+pt4[0]+pt3[0])//3, (pt1[1]+pt4[1]+pt3[1])//3)
    # cv2.circle(frame, centroid, 4, (0, 255, 0))
    mask = object_detector.apply(frame)
    countours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if area > 100:
            # cv2.drawContours(frame,[cnt],-1,(0,255,0),2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            ball_x, ball_y = x + (w) / 2, h
            # print('x :',ball_x,' y :' ,ball_y)

            list1.append(ball_x)
            list2.append(ball_y)

    # def bouncing (list1,list2):

    #     x_new  = list1[1]
    #     y_new = list2[1]
    #     new_list1 = []
    #     new_list2 = []
    #     new_list11 = []
    #     new_list21 = []
    #     final_list_x1 = []
    #     final_list_y1 = []
    #     final_list_x2 = []
    #     final_list_y2 = []

    #     for i in range(len(list1)):
    #             if(list1[i+1]>=x_new and list2[i+1]<=y_new):
    #                 if(list1[i+1]!=list1[i] or list2[i+1]!=list2[i]):
    #                     new_list1 = new_list1.append(list1[i+1])
    #                     new_list2 = new_list2.append(list2[i+1])
    #                 final_list_x1  =final_list_x1.append(new_list1[-1])
    #                 final_list_y1  =final_list_y1.append(new_list2[-1])
    #                 print(final_list_x1)
    #                 print(final_list_y1)
    #             elif(list1[i+1]<=x_new and list2[i+1]<=y_new):
    #                 if(list2[i+1]!=list2[i]):
    #                     new_list11.append(list1[i+1])
    #                     new_list21.append(list2[i+1])
    #                 final_list_x2.append(new_list1[-1])
    #                 final_list_y2.append(new_list2[-1])
    #                 print(final_list_x2)
    #                 print(final_list_y2)
    #             else:
    #                 break

    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
print('X :', list1)
print('Y :', list2)

bouncing(list1, list2)
cap.release()
cv2.destroyAllWindows()