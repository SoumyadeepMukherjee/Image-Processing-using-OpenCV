import cv2
import numpy as np

path="Resources/opencv.png"

def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Min", "Trackbars")
    s_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Hue Min", "Trackbars")
    v_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Hue Min", "Trackbars")

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResult=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)