import cv2

img=cv2.imread('CV2.png')
a=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresholdImg=cv2.threshold(a,150,260,cv2.THRESH_BINARY)[1]
cv2.imwrite("threshold1.jpg",thresholdImg)

