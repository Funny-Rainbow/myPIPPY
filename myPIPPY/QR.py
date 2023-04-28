import cv2
import numpy as np
from pyzbar.pyzbar import decode
from time import sleep
import os
import PIPPY
import robot

robotCtrl = PIPPY.PIPPY()
robotCtrl.start()

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        if barcodeData == 'forward' or barcodeData == 'backward' or barcodeData == 'left' or barcodeData == 'right':
            print(barcodeData)
            robotCtrl.moveStart(100, 'no', barcodeData)
            sleep(1)
            robotCtrl.moveStop()

        if barcodeData == 'forward' or barcodeData == 'backward' or barcodeData == 'left' or barcodeData == 'right':
            robotCtrl.moveStop()
        if barcodeData:
            barcodeData=None
            return(barcodeData)



if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            print(type(frame))
            cv2.imshow('Image', frame)
            code  =  decoder(frame)
            if code:
                print(code)

            code = cv2.waitKey(10)