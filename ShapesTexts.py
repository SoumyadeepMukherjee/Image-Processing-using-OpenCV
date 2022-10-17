import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)                # Produces a black image as zeros in an img implies black
# print(img)
# img[:]=255,0,0                                  #Coloring the whole img as blue

cv2.line(img,(0,0),(300,300),(0,255,0),3)         # Draws a line from starting pt to ending pt with a specified thickness

cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)   # Draws a rectangle from starting pt to ending pt filling it with a specific color

cv2.circle(img,(400,50),30,(255,255,0),5)           # Draws a circle with a specific centre pt, radius, a specific color and thickness

cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)   # Puts a specific text with a certain starting pt,font,scale,color and thickness

cv2.imshow("Image",img)

cv2.waitKey(0)

