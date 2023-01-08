import RPi.GPIO as GPIO
import time
import numpy as np
import cv2 , os
import threading
import datetime
import math
from motor import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)





video_capture = cv2.VideoCapture(-1)  # load /dev/video0

#카메라 설정
video_capture.set(cv2.CAP_PROP_FPS,20)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH ,320)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)



sp = 90
spgo = 60


motor = 0
if motor == 1:
    leftPWM.start(0) # pwm 시작
    rightPWM.start(0)
    frontPWM.start(0)
    backPWM.start(0)



stop()


count = 0
direction  = 0
while True:
    ret, frame2 = video_capture.read() #카메라 읽어옴
    frame2 = cv2.resize(frame2, dsize=(320,240), interpolation=cv2.INTER_AREA)
    mat = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY) #흑백으로 변환

    lower_white = np.array([0, 0, 0])
    upper_white = np.array([35, 35, 35])
    white_mask = cv2.inRange(frame2, lower_white, upper_white)
    cv2.imwrite('/home/pi/project/p.jpg', white_mask)
    frame1= cv2.imread('/home/pi/project/p.jpg')

    w = 320
    h = 240

    x = []
    y = []
    flag = False
    frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY) #흑백으로 변환
    #cv2.imwrite('/home/pi/project/pic.jpg', frame)
    ret,img= cv2.threshold(frame,127,255,cv2.THRESH_BINARY) #흰,검 으로 변환
    img= cv2.Canny(img,200,400) #윤곽선 추출
    img = img[160:240,0:320]
    #roi = frame2[110:160,0:320]

    lines = cv2.HoughLinesP(img, 1, np.pi / 180, 20)

    if(lines is not None):
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(frame2, (x1, y1+160), (x2, y2+160), (0, 0, 255), 2)
                x.extend([x1, x2])
                y.extend([y1, y2])
                flag = True

    min_y = int(img.shape[0] * 0.6)
    max_y = int(img.shape[0])

    font = cv2.FONT_HERSHEY_SIMPLEX

    if flag:
        poly = np.poly1d(np.polyfit(
            y,
            x,
            deg=1
        ))
        x_start = int(poly(max_y))
        x_end = int(poly(min_y))
        dx = int((x_end - x_start) * 0.23)
        dy = int(max_y - min_y)
        direction = math.atan2(dy, dx) / math.pi * 180 - 90
        print(direction)
        count = 0
    else:
        count += 1
    if count > 15:
        stop()
    else:
        if(direction < -6):
            right(sp)
        elif(direction > 6):
            left(sp)
        else:
            go(spgo)
    cv2.imwrite('/home/pi/project/pic.jpg', frame2)

    #drive.driveAngle(angle)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
video_capture.release()