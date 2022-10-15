#Reading images,videos and webcam

import cv2
print("Package imported")

#Reading & displaying images
img=cv2.imread("Resources/opencv.png")

cv2.imshow("Output",img)
cv2.waitKey(1000)   #The output screen waits for 1000s


#Reading & displaying videos
vid=cv2.VideoCapture("Path")

while True:
    sucess,img=vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):   #Quits the output screen on pressing 'q' on the keyboard
        break


#Reading & using the webcam
cam=cv2.VideoCapture(0)  #Id for webcam-0
cam.set(3,640)  #Width id-3
cam.set(4,480)  #Height id-4
cam.set(10,100) #Brightness id-10

while True:
    success, img = cam.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



