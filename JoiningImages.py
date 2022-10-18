import cv2
import numpy as np

img = cv2.imread("Resources/opencv.png")

imgHor = np.hstack((img,img))    # Joins or stacks the img in the horizontal direction side by side
imgVer = np.vstack((img,img))     # Joins or stacks the img in the vertical direction

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)

cv2.waitKey(0)
