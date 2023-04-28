#from base_camera import BaseCamera
import robot
import datetime
import time
import PIPPY

robotCtrl = PIPPY.PIPPY()
robotCtrl.start()

screenWidth = 640
screenHigh = 480


facecenterX = 1
facecenterY = 1
centerX = 320
centerY = 240
#posX = 1
#posY = 200
#posW = 200
#posH = 200

findfaceError = min(screenWidth, screenHigh) / 5
#cap = cv2.VideoCapture(0)

#def update():
 #   ret, frame = cap.read()
  #  if ret:
   #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #    hello=gray
     #   face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
      #  face = face_detect.detectMultiScale(gray)
       # for x,y,w,h in face:
        #   cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        #img = cv2.imread(img)
        #cv2.imshow('read_img',hello)
        #cv2.waitKey(0)


def track(posX, posY, posW, posH):
    print(posX, posY, posW, posH)
    facecenterX = posX + float(posW/2)
    facecenterY = posY + float(posH/2)
    centerX = float(screenWidth/2)
    centerY = float(screenHigh/2)
    if centerX - findfaceError > facecenterX :
        robotCtrl.moveStart(80, 'no', 'right')
        print('right')
        time.sleep(1)
        robotCtrl.moveStop()
        return 1
    if centerX + findfaceError < facecenterX :
        robotCtrl.moveStart(80, 'no', 'left')
        print('left')
        time.sleep(1)
        robotCtrl.moveStop()
        return 1
    if centerX - findfaceError < facecenterX and centerX + findfaceError > facecenterX:
        print('stay')
        return 0



if __name__ == '__main__':
    while(1):
        update()
        #Calculate()
        #if FacemoveX() == 0:
            #break
        #time.sleep(1)