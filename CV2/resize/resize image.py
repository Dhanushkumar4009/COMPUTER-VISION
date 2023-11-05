import cv2

img=cv2.imread('CV2.png')
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaussianImg=cv2.GaussianBlur(grayImg,(21,21),0)
cv2.imwrite('GaussianBlur.jpg',gaussianImg)
