import os
import cv2
#from base_camera import BaseCamera
import numpy as np


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        print('w')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hello=gray
        face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
        face = face_detect.detectMultiScale(gray)
        for x,y,w,h in face:
           cv2.rectangle(face,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        #img = cv2.imread(img)
        cv2.imshow('read_img',gray)