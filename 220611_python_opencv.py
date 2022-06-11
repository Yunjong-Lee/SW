### image와 동영상 동시 저장

import cv2
import datetime as dt


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

dispW=1600
dispH=900
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

#재생할 파일의 넓이와 높이
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

now = dt.datetime.now().strftime("%y%m%d_%H%M%S_%M")

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter("D:/" + str(now) + ".avi", fourcc, 30.0, (int(width), int(height)))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == False:  
        break;
        
    real_time = dt.datetime.now().strftime("%y%m%d_%H%M%S_%f")    
    cv2.rectangle(frame, (2,2), (250,24), (255,255,255), cv2.FILLED)
    cv2.putText(frame, real_time,(4,18), cv2.FONT_HERSHEY_PLAIN,0.9,(1,1,1))        
    
    cv2.imshow('frame',frame)
    cv2.imwrite(str(real_time) + '.jpg',frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
