import cv2
import numpy as np

img=cv2.imread("Resources/opencv.png")
print(img.shape)

#Resizing the image with new height and width
imgResize=cv2.resize(img,(200,100))

#Cropping the req image acc to the specifications
imgCropped=img[0:100,100:150]   #Height comes before width in the img matrix

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image cropped",imgCropped)

cv2.waitKey(0)