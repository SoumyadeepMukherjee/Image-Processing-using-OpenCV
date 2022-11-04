import cv2
import numpy as np

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)   #find the all extreme outer contours of the img (Parameters: img,retrieval method,approx func.)
    for cnt in contours:
        area=cv2.contourArea(cnt)      #finds the area of the contour
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)    #draws lines over the contours
            peri=cv2.arcLength(cnt,True)
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)       #finds the edges over the perimeter of the shape
            print(len(approx))
            objCor=len(approx)       #finds the num of corners of an obj
            x,y,w,h=cv2.boundingRect(approx)    #creates a bounding rect over the shape

            #Checks for various shapes
            if objCor==3:
                objectType="Tri"
            elif objCor==4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:
                    objectType="Sq"
                else:
                    objectType="Rect"
            elif objCor==5:
                objectType="Penta"
            elif objCor==6:
                objectType="Hexa"
            elif objCor==8:
                objectType="Octa"
            else:
                objectType="Circle"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)          #Draws a rect over the img contour
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,
                         (0,0,0),2)                                        #Puts corresponding texts over the shapes


shapes='Resources/shapes.jpg'
img=cv2.imread(shapes)
imgContour=img.copy()

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Converting to Gray scale img
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)     #Blurring the gray scale img
imgCanny=cv2.Canny(imgBlur,50,50)             #Finds the edges of the blurred img
getContours(imgCanny)

#cv2.imshow("Original",img)
#cv2.imshow("Gray",imgGray)
#cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Contour",imgContour)

cv2.waitKey(0)