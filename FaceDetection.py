import cv2

TrainedDataSet=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Capture=cv2.VideoCapture(0)

while True:
    _,Frame=Capture.read()
    GrayImg=cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    Faces=TrainedDataSet.detectMultiScale(GrayImg)
    print(Faces)
    for x,y,w,h in Faces:
        cv2.rectangle(Frame,(x,y),(x+h,y+w),(255,0,0),2)
    cv2.imshow("FaceDetection",Frame)
    k=cv2.waitKey(1)
    if k==ord('q') &0XFF:
        break
Capture.release()
cv2.destroyAllWindows()

