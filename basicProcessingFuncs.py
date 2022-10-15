import cv2
import numpy as np

img=cv2.imread("Resources/opencv.png")     #Reading the image from resources
kernel=np.ones((5,5),np.uint8)             #Making a 5x5 kernel with all ones

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)           #Converting from color to gray scale image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)              #Converting from gray to blurred image
imgCanny=cv2.Canny(img,150,200)                        #Converting from color to canny image with lots of edges
imgDilation=cv2.dilate(imgCanny,kernel,iterations=5)   #Dilating or thickening the edges of the canny image
imgEroded=cv2.erode(imgDilation,kernel,iterations=1)   #Eroding or thinning the edges of the dilated image


cv2.imshow("Gray image",imgGray)
cv2.imshow("Blurred image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dilation image",imgDilation)
cv2.imshow("Eroded image",imgEroded)
cv2.waitKey(0)
