import cv2

img=cv2.imread('CV2.png')
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaussImg1=cv2.GaussianBlur(grayImg,(21,21),0)
thresholdImg=cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("threshold.jpg",thresholdImg)

